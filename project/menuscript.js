


const featuredItems = [
  {
    name: "3D Rose Gelatin Cake",
    image: "images/item1.jpg",
    description: "Handcrafted gelatin flower art",
  },
  {
    name: "Strawberry Mousse",
    image: "images/item2.jpg",
    description: "Light and fruity delight",
  },
  {
    name: "Mini Cupcake Box",
    image: "images/item3.jpg",
    description: "Perfect for parties & gifts",
  }
];

function renderFeaturedItems() {
  const container = document.getElementById("featured-items");
  container.innerHTML = ""; // Clear before rendering

  featuredItems.forEach((item) => {
    const card = document.createElement("div");
    card.className = "item-card";
    card.innerHTML = `
      <img src="${item.image}" alt="${item.name}" loading="lazy">
      <h3>${item.name}</h3>
      <p>${item.description}</p>
    `;
    container.appendChild(card);
  });
}

// Save and retrieve user visit info
function saveVisitCount() {
  const key = "visitCount";
  let count = localStorage.getItem(key);
  count = count ? parseInt(count) + 1 : 1;
  localStorage.setItem(key, count);

  if (count === 1) {
    console.log(`Welcome! This is your first visit.`);
  } else {
    console.log(`Welcome back! You've visited ${count} times.`);
  }
}

// Run features on load
document.addEventListener("DOMContentLoaded", () => {
  renderFeaturedItems();
  saveVisitCount();
});