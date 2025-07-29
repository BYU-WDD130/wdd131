// Dessert data
const menuItems = [
  {
    name: "Red Velvet Cake",
    type: "cake",
    image: "images/redvelvet.jpg",
    price: 20
  },
  {
    name: "Classic Chocolate Chip Cookies",
    type: "cookie",
    image: "images/cookies.jpg",
    price: 12
  },
  {
    name: "Raspberry Macarons",
    type: "macaron",
    image: "images/macarons.jpg",
    price: 18
  },
  {
    name: "Strawberry Shortcake",
    type: "cake",
    image: "images/strawberryshortcake.jpg",
    price: 22
  }
];

// Render items based on filter
function renderMenuItems(items) {
  const container = document.getElementById("menu-items");
  container.innerHTML = "";

  if (items.length === 0) {
    container.innerHTML = "<p>No items match your filter.</p>";
    return;
  }

  items.forEach(item => {
    const card = document.createElement("div");
    card.className = "item-card";

    card.innerHTML = `
      <img src="${item.image}" alt="${item.name}" loading="lazy">
      <h3>${item.name}</h3>
      <p>$${item.price.toFixed(2)}</p>
    `;

    container.appendChild(card);
  });
}

// Filter function with conditional logic
function filterMenu(type) {
  const filtered = type === "all"
    ? menuItems
    : menuItems.filter(item => item.type === type);

  renderMenuItems(filtered);
  localStorage.setItem("lastFilter", type); // store last filter
}

// Load last used filter on page load
window.addEventListener("DOMContentLoaded", () => {
  const savedFilter = localStorage.getItem("lastFilter") || "all";
  filterMenu(savedFilter);
});