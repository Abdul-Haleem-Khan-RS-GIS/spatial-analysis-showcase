// Contact form: send in the background through FormSubmit's AJAX endpoint.
// If FormSubmit cannot be reached (some networks block it), open the visitor's
// email app with the message already filled in, so no enquiry is lost.
(function () {
  var form = document.getElementById('contact-form');
  if (!form) return;
  var status = document.getElementById('form-status');
  var btn = form.querySelector('button[type=submit]');
  var to = form.getAttribute('data-email');

  function show(msg, kind) {
    status.textContent = '';
    status.className = 'form-status ' + (kind || '');
    status.insertAdjacentHTML('beforeend', msg);
    status.hidden = false;
  }
  function mailtoLink() {
    var f = new FormData(form);
    var body = 'Name: ' + (f.get('name') || '') + '\nEmail: ' + (f.get('email') || '') +
      '\nProject / organisation: ' + (f.get('project') || '') + '\n\n' + (f.get('message') || '');
    return 'mailto:' + to + '?subject=' + encodeURIComponent('Portfolio enquiry from ' + (f.get('name') || 'website')) +
      '&body=' + encodeURIComponent(body);
  }
  function fallback() {
    var link = mailtoLink();
    show('Your network blocked the message service, but your message is ready. Tap the button to send it from your email app:' +
         '<br><a class="btn" style="margin-top:10px;display:inline-block" href="' + link + '">Send by email</a>' +
         '<br><span style="font-size:14px">Or write directly to <a href="mailto:' + to + '">' + to + '</a>.</span>', 'warn');
  }

  form.addEventListener('submit', function (e) {
    if (!window.fetch || !window.FormData) return;            // very old browsers: normal form post
    e.preventDefault();
    if (form.querySelector('[name=_honey]').value) return;    // spam trap
    btn.disabled = true; var label = btn.textContent; btn.textContent = 'Sending…';
    var data = new FormData(form);
    data.delete('_next'); data.delete('_captcha');
    var ctrl = window.AbortController ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, 15000);
    fetch('https://formsubmit.co/ajax/' + to, {
      method: 'POST', body: data, headers: {Accept: 'application/json'}, signal: ctrl ? ctrl.signal : undefined
    }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return {ok: r.ok, j: j}; }); })
      .then(function (res) {
        clearTimeout(timer);
        if (res.ok && String(res.j.success) === 'true') {
          form.reset();
          show('Thank you, your message has been sent. I usually reply within a few hours.', 'ok');
        } else { fallback(); }
      })
      .catch(function () { clearTimeout(timer); fallback(); })
      .then(function () { btn.disabled = false; btn.textContent = label; });
  });
})();
