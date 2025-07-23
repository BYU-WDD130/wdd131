//actual year
document.getElementById("currentyear").textContent = new Date().getFullYear();
//last modification
document.getElementById("LastModified").textContent = "Last Modified: " + document.lastModified;


document.addEventListener("DOMContentLoaded", function () { 
//elementos del menu movil
  const menuButton = document.getElementById("menu"); 
  const mobileMenu = document.getElementById("mobile-menu"); 

  
//abrir menu
  menuButton.addEventListener("click", () => { 
  mobileMenu.classList.add("active"); 
  });

//cerrar menu
const navLinks = mobileMenu.querySelectorAll("a");
navLinks.forEach(link =>{
link.addEventListener("click" , () => {
  closeMenuBtn.addEventListener("click", () => { 
    mobileMenu.classList.remove("active"); 
     });
   });
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
});


  




 



