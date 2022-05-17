const hamburgerMenu = document.querySelector("#navigation .nav-icon");
const navContent = document.querySelector("#nav-content");
const closeBtn = document.querySelector("#nav-content .close-btn");
const navLinks = document.querySelectorAll("#nav-content nav ul li a");
const scrollTop = document.querySelector(".scroll-top");

if (scrollTop) {
  window.addEventListener("scroll", function () {
    if (pageYOffset > window.innerHeight * 1.2) {
      //100vh vayo total height edi window ko innerheight 1.2 tali tala scroll garda
      scrollTop.style.display = "flex";
    } else {
      scrollTop.style.display = "none";
    }
  });
  scrollTop.addEventListener("click", function () {
    window.scrollTo(0, 0); //x axis 0 ani y axis 0 basically top vanya
  });
}

hamburgerMenu.addEventListener("click", function () {
  navContent.classList.add("show");
  document.body.style.overflow = "hidden";
});
closeBtn.addEventListener("click", function () {
  navContent.classList.remove("show");
  document.body.style.overflow = "initial";
});

navLinks.forEach(function (link) {
  link.addEventListener("click", function () {
    navContent.classList.remove("show");
    document.body.style.overflow = "initial";
  });
});
