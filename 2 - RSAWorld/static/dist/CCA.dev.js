"use strict";

var channel = 0;
var cipher_text = 238947;
fetch('../static/channel-in.txt') // fetch text file
.then(function (resp) {
  return resp.text();
}).then(function (data) {
  channel = data.split(/\r?\n/);
  cipher_text = String(channel.at(-1));
  console.log(cipher_text);
});

var modExp = function modExp(a, b, n) {
  a = a % n;
  var result = 1;
  var x = a;

  while (b > 0) {
    var leastSignificantBit = b % 2;
    b = Math.floor(b / 2);

    if (leastSignificantBit == 1) {
      result = result * x;
      result = result % n;
    }

    x = x * x;
    x = x % n;
  }

  return result;
};

var n = 0;
var e = 0;
var d = 0;
var hack_text = 0;
var two_e = 0;
var d_hack_text = 0; // decrypted hack text

var hacked_msg = 0;
var real_msg = 0;

function set_cipher_text() {
  var elem = document.getElementById('cca-ciphertext');
  two_e = modExp(2, e, n);
  hack_text = cipher_text * two_e % n;
  d_hack_text = modExp(hack_text, d, n);
  hacked_msg = d_hack_text % 2 == 0 ? d_hack_text / 2 : (d_hack_text + n) / 2;
  real_msg = modExp(cipher_text, d, n);
  elem.innerHTML = String(hack_text);
}

function show() {
  var key = document.getElementById('my-data');
  n = parseInt(key.getAttribute('n'));
  e = parseInt(key.getAttribute('e'));
  d = parseInt(key.getAttribute('d'));
  name = key.getAttribute('name');
  set_cipher_text();
  var elem = document.getElementById('darth');
  var audio = document.getElementById("audio");
  elem.style.display = "block";
  audio.volume = 1.0;
  audio.play();
}

function hide() {
  var audio = document.getElementById("audio");
  var elem = document.getElementById('darth');
  elem.style.display = "none";
  audio.pause();
  audio.currentTime = 0;
}

function show_hack() {
  hide();
  var content = document.getElementById('hack-content');
  content.innerHTML = "\n      <span style=\"color: yellow; font-size:1.9rem; margin:auto; display:table;\">You have been compromised. </span> <br>\n      I was interested in exposing your most recent message which had $$C = ".concat(cipher_text, " $$\n      <br>\n      So I first computed<br> $$2^{e}\\:mod\\:n = 2^{").concat(e, "}\\:mod\\:").concat(n, " =  ").concat(two_e, " $$\n      <br>\n      and then I took as a chosen ciphertext <br>\n       $$ Y = C \\times (2^{e} \\:mod\\:n) \\:mod\\:n = ").concat(cipher_text, " \\times ").concat(two_e, " \\:mod \\: ").concat(n, " =  ").concat(hack_text, " $$\n      <br>\n      By asking you to sign this, you implictly provided me with\n      <br>   \n      $$ X = Y^{d} \\: mod \\: n = (C \\times 2^{e} )^{d} \\: mod \\: n = ").concat(d_hack_text, "$$ \n      <br>\n      then because as well $gcd(2, n) = 1$, we have\n      <br>\n      $$ M =  2^{-1} \\times X \\: mod \\: n = 2^{-1} \\times ").concat(d_hack_text, " \\: mod \\: ").concat(n, " = ").concat(hacked_msg, "$$\n      <br>\n      Which is you original message.\n      ");
  MathJax.Hub.Queue(["Typeset", MathJax.Hub, content]);
  var elem = document.getElementById('hacked');
  var audio = document.getElementById("audio1");
  elem.style.display = "block";
  audio.volume = 1.0;
  audio.play();
}

function hide_hack() {
  var elem = document.getElementById('hacked');
  elem.style.display = "none";
  var audio = document.getElementById("audio1");
  audio.pause();
  audio.currentTime = 0;
}

function CCA() {
  hide();
  show_hack();
}

window.onload = function () {
  var key = document.getElementById('my-data');
  n = parseInt(key.getAttribute('n'));
  e = parseInt(key.getAttribute('e'));
  d = parseInt(key.getAttribute('d'));
  set_cipher_text();
  document.addEventListener("keypress", function (event) {
    if (event.keyCode === 49) {
      event.preventDefault();
      show();
    }
  });
};