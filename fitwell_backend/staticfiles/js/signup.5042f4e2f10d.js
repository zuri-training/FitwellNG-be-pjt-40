window.onload = (e) => {
  let current_fs, next_fs; //fieldsets
  button1 = document.getElementById('next1');
  button1.onclick = (e) => {
    alert("next clikced");
    current_fs = button1.parentElement.parentElement;
    next_fs = button1.parentElement.parentElement.nextElementSibling;
    current_fs.style.display = 'none';
    next_fs.style.display = 'block';
    document.getElementById('img').style.backgroundImage =
      'url(/static/images/sign-up-bg2.png)';
    step1 = document.getElementById('step1').classList.add('active');
  };

  button2 = document.getElementById('next2');
  button2.onclick = (e) => {
    current_fs = button2.parentElement.parentElement;
    next_fs = button2.parentElement.parentElement.nextElementSibling;
    current_fs.style.display = 'none';
    next_fs.style.display = 'block';
    console.log(document.getElementById('img').style.background);
    step1 = document.getElementById('step2').classList.add('active');
    document.getElementById('img').style.backgroundImage =
      'url(/static/images/sign-up-bg3.png)';
  };
};
