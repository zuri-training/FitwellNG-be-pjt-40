let navBar = document.querySelector(".navbar");
let hamburger = document.querySelector(".hamburger-menu");

const toggle = () => {
    navBar.classList.toggle("active");
}
hamburger.addEventListener("click", toggle);