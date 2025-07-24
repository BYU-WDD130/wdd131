


//actual year
document.getElementById("currentyear").textContent = new Date().getFullYear();
//last modification
document.getElementById("LastModified").textContent = "Last Modified: " + document.lastModified;


const menuButton = document.getElementById("menu");
const mobileMenu = document.getElementById("mobileMenu");

menuButton.addEventListener("click", () => {
  mobileMenu.classList.toggle("active");
  

  if (mobileMenu.classList.contains("active")) {
    menuButton.textContent = "✖";
  } else {
    menuButton.textContent = "☰";
  }
});

//menu hamburgueza (para navegacion principal)

  const hamButton = document.querySelector('#menu');
  const navigation = document.querySelector('.navigation');
  const title = document.querySelector('#title');
  const header = document.querySelector("header");

  hamButton.addEventListener('click', () => {
   navigation.classList.toggle('open');
   hamButton.classList.toggle('open');
   header.classList.toggle("open");
   title.classList.toggle('hide');
  });


