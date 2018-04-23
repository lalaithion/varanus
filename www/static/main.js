var tokens_display = document.getElementById('tokens-display');
var logging_display = document.getElementById('logging-display');
var alerts_display = document.getElementById('alerts-display');
var kv_display = document.getElementById('management-kv-display')
var tokens_template = document.getElementById('tokens-template');
var logging_template = document.getElementById('logging-template');
var alerts_template = document.getElementById('alerts-template');
var kv_template = document.getElementById('management-kv-template')
var management_selected = document.getElementById('management-selected');
var management_status = document.getElementById('management-status');

var tokens = [
  {
    type: 'user',
    secure: true,
    fname: 'Jenna',
    lname: 'Riggen',
    email: 'jenna.riggen@colorado.edu',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'user',
    secure: false,
    fname: 'Izaak',
    lname: 'Anderson',
    email: 'izaak.anderson@colorado.edu',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'user',
    secure: true,
    fname: 'Daisy',
    lname: 'Haskell',
    email: 'daisy.haskell@colorado.edu',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'card',
    secure: true,
    fname: 'Izaak',
    lname: 'Anderson',
    num: '1378 2394 4279 1243',
    exp: '5/26 2021',
    address: '420 28th st',
    country: 'United States',
    state: 'Colorado',
    city: 'Boulder',
    zip: '80302',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'card',
    secure: false,
    fname: 'Jenna',
    lname: 'Riggen',
    num: '9867 2348 1925 1285',
    exp: '8/29 2021',
    address: '1111 Engineering Drive',
    country: 'United States',
    state: 'Colorado',
    city: 'Boulder',
    zip: '80309',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'number',
    secure: true,
    number: '555 235 9536',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'number',
    secure: true,
    number: '555 765 1324',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'number',
    secure: true,
    number: '555 268 0891',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
]

function shortName(e) {
  if(e.type == 'user') {
    return e.fname + ' ' + e.lname;
  }
  if(e.type == 'card') {
    return e.num;
  }
  if(e.type == 'number') {
    return e.number;
  }
  if(e.type == 'log') {
    return e.date + ' ' + e.time;
  }
}

for(var token of tokens) {
  var icons = {
    user: 'fa-user',
    card: 'fa-credit-card',
    number: 'fa-phone-square',
  }
  var status_icon = token.secure ? 'fa-lock' : 'fa-exclamation-circle';
  var display_text = document.createTextNode(shortName(token));
  new_token = tokens_template.cloneNode(true);
  new_token.removeAttribute('id');
  new_token.classList.add(token.secure ? 'secure' : 'insecure');
  new_token.getElementsByClassName('type')[0].classList.add(icons[token.type]);
  new_token.getElementsByClassName('status')[0].classList.add(status_icon);
  new_token.insertBefore(display_text, new_token.childNodes[2]);
  new_token.style.display = '';
  new_token.onclick = ((e) => () => manage(e))(token);
  tokens_display.appendChild(new_token);
}

var logs = [
  {
    type: 'log',
    secure: true,
    date: '32-12-2018',
    time: '03:12',
    hash: '2b00042f7481c7b056c4b410d28f33cf',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'log',
    secure: false,
    date: '32-12-2018',
    time: '03:34',
    hash: 'd8b74df393528d51cd19980ae0aa028e',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'log',
    secure: false,
    date: '32-12-2018',
    time: '03:46',
    hash: 'd8b74df393528d51cd19980ae0aa028e',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'log',
    secure: true,
    date: '32-12-2018',
    time: '03:58',
    hash: 'd8b74df393528d51cd19980ae0aa028e',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'log',
    secure: true,
    date: '32-12-2018',
    time: '04:10',
    hash: 'd8b74df393528d51cd19980ae0aa028e',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'log',
    secure: true,
    date: '32-12-2018',
    time: '04:22',
    hash: 'd8b74df393528d51cd19980ae0aa028e',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'log',
    secure: true,
    date: '32-12-2018',
    time: '04:34',
    hash: 'd8b74df393528d51cd19980ae0aa028e',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
  {
    type: 'log',
    secure: true,
    date: '32-12-2018',
    time: '04:46',
    hash: 'd8b74df393528d51cd19980ae0aa028e',
    alerts: [
      {
        type: 'email',
        location: 'admin@varanus.com'
      },
      {
        type: 'number_call',
        location: '555 207 1245'
      },
    ],
  },
]

for(var log of logs) {
  var status_icon = log.secure ? 'fa-lock' : 'fa-exclamation-circle';
  var display_text = document.createTextNode(shortName(log));
  new_log = logging_template.cloneNode(true);
  new_log.removeAttribute('id');
  new_log.classList.add(log.secure ? 'secure' : 'insecure');
  new_log.getElementsByClassName('status')[0].classList.add(status_icon);
  new_log.insertBefore(display_text, new_log.childNodes[1]);
  new_log.style.display = '';
  new_log.onclick = ((e) => () => manage(e))(log);
  logging_display.appendChild(new_log);
}

function manage(entry) {
  if(entry.type != 'log') {
    management_selected.innerHTML = 'Honey-' + entry.type + ': ' + shortName(entry);
  }
  else {
    management_selected.innerHTML = 'Log: ' + shortName(entry);
  }

  var status_icon = entry.secure ? 'fa-lock' : 'fa-exclamation-circle';
  management_status.childNodes[1].innerHTML = entry.secure ? 'Secured' : 'Breached!';
  management_status.childNodes[2].className = 'right fa ' + status_icon;
  management_status.className = entry.secure ? 'secure' : 'insecure';

  alerts_display.innerHTML = '';
  for(var alert of entry.alerts) {
    var icons = {
      email: 'fa-envelope',
      number_call: 'fa-phone-square',
      number_text: 'fa-mobile-alt',
    }
    var display_text = document.createTextNode(alert.location);
    var new_alert = alerts_template.cloneNode(true);
    new_alert.removeAttribute('id');
    new_alert.getElementsByClassName('type')[0].classList.add(icons[alert.type]);
    new_alert.insertBefore(display_text, new_alert.childNodes[2]);
    new_alert.style.display = '';
    alerts_display.appendChild(new_alert);
  }
  kv_display.innerHTML = '';
  for(var key in entry) {
    if(key == 'alerts' || key == 'type' || key == 'secure') {
      continue;
    }
    var value = entry[key];
    var new_kv = kv_template.cloneNode(true);
    new_kv.removeAttribute('id');
    new_kv.childNodes[1].innerHTML = key;
    new_kv.childNodes[5].innerHTML = value;
    new_kv.style.display = '';
    kv_display.appendChild(new_kv);
  }
}

function add_alert() {
  console.log(arguments);
  console.log(this);
}

manage(tokens[0])
