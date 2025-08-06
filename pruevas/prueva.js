const featuredItems = [
  {
    name: "Rose Must",
    price: "$45.50",
    description: "Delicate strawberry gelatin mousse",
    image: "images/coldcake.webp"
  },
  {
    name: "Fruit Cake",
    price: "$5.00",
    description: "Classic delightful fruit cake",
    image: "images/frutecake3.webp"
  },
  {
    name: "Vanilla Cupcake",
    price: "$3.50",
    description: "Soft vanilla cupcake with buttercream",
    image: "images/cupcake.webp"
  },
  {
    name: "Mango Mousse",
    price: "$4.25",
    description: "Creamy mango mousse in a cup",
    image: "images/mango-mousse.webp"
  }
];

function renderFeaturedItems(items) {
  const container = document.getElementById("customer-favorites");
  if (!container) return;

  container.innerHTML = "";
  items.forEach(item => {
    const card = document.createElement("div");
    card.className = "item-card";
    card.innerHTML = `
      <img src="${item.image}" alt="${item.name}" loading="lazy">
      <h3>${item.name}</h3>
      <p>${item.description}</p>
      <strong>${item.price}</strong>
    `;
    container.appendChild(card);
  });

  localStorage.setItem("featured", JSON.stringify(items));
}

renderFeaturedItems(featuredItems);

document.getElementById("currentyear").textContent = new Date().getFullYear();