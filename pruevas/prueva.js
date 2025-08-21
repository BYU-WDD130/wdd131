// script.js
document.addEventListener("DOMContentLoaded", () => {
  // Set dynamic year
  const yearEl = document.getElementById("currentyear");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // Load featured products
  const featuredItems = [
    { name: "3D Rose Gelatin", img: "images/rose-jelly.webp" },
    { name: "ChocoFlan Cake", img: "images/chocoflan1.webp" },
    { name: "Fruit Mousse", img: "images/mousse.webp" }
  ];

  const container = document.getElementById("featured-items");
  if (container) {
    featuredItems.forEach(item => {
      const card = document.createElement("div");
      card.className = "items-card";
      card.innerHTML = `
        <img src="${item.img}" alt="${item.name}" loading="lazy">
        <h3>${item.name}</h3>
      `;
      container.appendChild(card);
    });
  }
});