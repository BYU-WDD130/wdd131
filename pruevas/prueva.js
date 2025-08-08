const featuredItems = [
  {
    name: "3D Rose Gelatin Cake",
    category: "3DJelly",
    price: "$35",
    image: "images/3djelly.webp",
    description: "Handcrafted gelatin flower art",
  },
  {
    name: "Strawberry Mousse",
    category: "cake",
    price: "$25",
    image: "images/coldcake.webp",  
    description: "Light and fruity delight",
  },
  {
    name: "Special dad cake",
    category: "cake",
    price: "$30",
    image: "images/dadcake2.webp",
    description: "Perfect for parties & gifts",
  },
  {
    name: "Blueberry Shortcake",
    category: "cake",
    price: "$25",
    image: "images/blueberry2.webp",
  },
  {
    name: "Chocolate Mousse Cake",
    category: "cake",
    price: "$28",
    image: "images/chocoflan2.webp",
  },
  {
    name: "Classic Semita Cookies",
    category: "cookie",
    price: "$10/dozen",
    image: "images/semita2.webp",
  },
  {
    name: "Pineapple jelly",
    category: "cake",
    price: "$35",
    image: "images/pineaplecake.webp",
  },
];

function filterMenu(category) {
  let itemsToShow = [];

  if (category === "all") {
    itemsToShow = featuredItems;
  } else {
    itemsToShow = featuredItems.filter(item => item.category === category);
  }

  displayMenuItems(itemsToShow);
}

function displayMenuItems(items) {
  const container = document.getElementById("menu-items");
  container.innerHTML = "";

  if (items.length === 0) {
    container.innerHTML = "<p>No items found.</p>";
    return;
  }

  items.forEach(item => {
    const card = document.createElement("div");
    card.className = "item-card";
    card.innerHTML = `
      <img src="${item.image}" alt="${item.name}" loading="lazy">
      <h3>${item.name}</h3>
      <p>${item.description || item.price || ''}</p>
    `;
    container.appendChild(card);
  });
}

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

document.addEventListener("DOMContentLoaded", () => {
  displayMenuItems(featuredItems);
  saveVisitCount();
});