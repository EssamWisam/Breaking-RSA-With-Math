var channel = 0;
var cipher_text = 238947;
fetch('../static/channel-in.txt') // fetch text file
  .then((resp) => resp.text())
  .then(data => {
    channel= data.split(/\r?\n/);
    cipher_text = String(channel.at(-1));
    console.log(cipher_text)

  }) 

  function Num2Str(num) {
    var str = "";
    //convert to binary
    num = num.toString(2);
    //pad with zeros until length is a multiple of 8
    num = num.padStart(8*Math.ceil(num.length/8), "0");
    //convert every 8 bits to a character
    for (var i = 0; i < num.length / 8; i++) {
      str += String.fromCharCode(parseInt(num.substr(i * 8, 8), 2));
    }
    return str;
  }

var modExp = function(a, b, n) {
  a = a % n;
  var result = 1;
  var x = a;

  while(b > 0){
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
var d_hack_text = 0;          // decrypted hack text
var hacked_msg = 0;
var real_msg = 0;




function set_cipher_text(){
      const elem = document.getElementById('cca-ciphertext');
      two_e = modExp(2, e, n );
      hack_text = (cipher_text * two_e) % n;
      d_hack_text = modExp(hack_text, d, n);
      hacked_msg = (d_hack_text % 2 == 0) ? d_hack_text/2 : (d_hack_text + n)/2; 
      hacked_msg = Num2Str(hacked_msg)
      real_msg = modExp(cipher_text, d, n);
      elem.innerHTML = String(hack_text);

    }

function show(){
      var key = document.getElementById('my-data');
      n = parseInt(key.getAttribute('n'));
      e = parseInt(key.getAttribute('e'));
      d = parseInt(key.getAttribute('d'));
      name = key.getAttribute('name');
  
      set_cipher_text();
      const elem = document.getElementById('darth');
      const audio = document.getElementById("audio");  
      elem.style.display= "block";
      audio.volume = 1.0;
      audio.play();
    }

function hide(){
    const audio = document.getElementById("audio");  
      const elem = document.getElementById('darth');
      elem.style.display= "none";
      audio.pause();
      audio.currentTime = 0;
    }

    function show_hack(){
      hide();
      const content = document.getElementById('hack-content');
      content.innerHTML = `
      <span style="color: yellow; font-size:1.9rem; margin:auto; display:table;">You have been compromised. </span> <br>
      I was interested in exposing your most recent message which had $$C = ${cipher_text} $$
      <br>
      So I first computed<br> $$2^{e}\\:mod\\:n = 2^{${e}}\\:mod\\:${n} =  ${two_e} $$
      <br>
      and then I took as a chosen ciphertext <br>
       $$ Y = C \\times (2^{e} \\:mod\\:n) \\:mod\\:n = ${cipher_text} \\times ${two_e} \\:mod \\: ${n} =  ${hack_text} $$
      <br>
      By asking you to sign this, you implictly provided me with
      <br>   
      $$ X = Y^{d} \\: mod \\: n = (C \\times 2^{e} )^{d} \\: mod \\: n = ${d_hack_text}$$ 
      <br>
      then because as well $gcd(2, n) = 1$, we have
      <br>
      $$ M =  2^{-1} \\times X \\: mod \\: n = 2^{-1} \\times ${d_hack_text} \\: mod \\: ${n} = ${hacked_msg}$$
      <br>
      Which is you original message.
      `;
      MathJax.Hub.Queue(["Typeset", MathJax.Hub, content]);
      const elem = document.getElementById('hacked');
      const audio = document.getElementById("audio1");  
      elem.style.display= "block";
      audio.volume = 1.0;
      audio.play();
    }

    function hide_hack(){
      const elem = document.getElementById('hacked');
      elem.style.display= "none";
      const audio = document.getElementById("audio1");  
      audio.pause();
      audio.currentTime = 0
    }

    function CCA(){
      hide();
      show_hack();

    }


  window.onload = function () {
  var key = document.getElementById('my-data');
  n = parseInt(key.getAttribute('n'));
  e = parseInt(key.getAttribute('e'));
  d = parseInt(key.getAttribute('d'));
  set_cipher_text();

  document.addEventListener("keypress", (event)=> {
      if (event.keyCode === 49) { 
        event.preventDefault();
        show();
      }
    });

  }