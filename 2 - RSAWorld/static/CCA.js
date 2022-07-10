var channel = 0;
var cipher_text = 238947;


var n = 0;
var name = 0;
var e = 0;
var d = 0;
var hack_text = 0;
var two_e = 0;
var d_hack_text = 0;          // decrypted hack text
var hacked_msg = 0;
var hack_text_str = '';
var hacked_msg_n = 0;
var real_msg = 0;


function set_cipher_text(){
      const elem = document.getElementById('cca-ciphertext');
      var key = document.getElementById('my-data');
      two_e = parseInt(key.getAttribute('two_e'));
      hack_text = parseInt(key.getAttribute('hack_text'));
      hack_text_str = key.getAttribute('hack_text_str');
      d_hack_text = parseInt(key.getAttribute('d_hack_text'));
      real_msg = parseInt(key.getAttribute('real_msg'));
      hacked_msg = key.getAttribute('hacked_msg');
      hacked_msg_n = key.getAttribute('hacked_msg_n');

      console.log(hacked_msg)
      console.log("GG")
      cipher_text = parseInt(key.getAttribute('cipher_text'));
      elem.innerHTML = String(hack_text_str);
    }

function show(){
      var key = document.getElementById('my-data');
      n = parseInt(key.getAttribute('n'));
      e = parseInt(key.getAttribute('e'));
      d = parseInt(key.getAttribute('d'));
  
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
      I was interested in exposing your most recent encrypted message which had $$C = ${cipher_text} $$
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
      $$ M =  2^{-1} \\times X \\: mod \\: n = 2^{-1} \\times ${d_hack_text} \\: mod \\: ${n} = ${hacked_msg_n}  $$
      <br>
      Which is equivalent to your original message: <span style="color: yellow; ">${hacked_msg} </span>
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