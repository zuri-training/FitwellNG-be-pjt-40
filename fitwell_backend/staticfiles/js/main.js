window.addEventListener("scroll", ()=>{
    const top = document.querySelector('.totop');
    top.classList.toggle('scrollup', scrollY > 200)
})