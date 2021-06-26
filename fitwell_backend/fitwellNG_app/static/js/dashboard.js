let navBar = document.querySelector(".navbar");
let links = document.querySelector(".links");
let hamburger = document.querySelector(".hamburger-menu");

const toggle = () => {
    links.classList.toggle("active");
    
    if(links.classList.value !== "links active") {
        navBar.style.height = "16vh";
    }
    else {
        navBar.style.height = "100vh";
    }
}
hamburger.addEventListener("click", toggle);