// Animación de entrada para el overlay
document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.querySelector('.overlay');
  overlay.style.opacity = 0;
  overlay.style.transform = 'translateY(20px)';
  setTimeout(() => {
    overlay.style.transition = 'all 0.8s ease';
    overlay.style.opacity = 1;
    overlay.style.transform = 'translateY(0)';
  }, 100);
});