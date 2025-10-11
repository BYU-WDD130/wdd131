
const nav = document.querySelector("#nav");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");

abrir.addEventListener("click", () => {
    nav.classList.add("visible");
})

cerrar.addEventListener("click", () => {
    nav.classList.remove("visible");
})

  const carousel = document.querySelector('.carousel-images');
  const images = document.querySelectorAll('.carousel-images img');
  const prevBtn = document.querySelector('.prev');
  const nextBtn = document.querySelector('.next');

  let index = 0;
  const total = images.length;
  let autoSlide = setInterval(nextImage, 3000); // cambia cada 3 segundos

  function showImage() {
    carousel.style.transform = `translateX(${-index * 100}%)`;
  }

  function nextImage() {
    index = (index + 1) % total;
    showImage();
  }

  function prevImage() {
    index = (index - 1 + total) % total;
    showImage();
  }

  // Botones
  nextBtn.addEventListener('click', () => {
    nextImage();
    resetAutoSlide();
  });

  prevBtn.addEventListener('click', () => {
    prevImage();
    resetAutoSlide();
  });

  // Reinicia el temporizador si el usuario usa los botones
  function resetAutoSlide() {
    clearInterval(autoSlide);
    autoSlide = setInterval(nextImage, 3000);
  }