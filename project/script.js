const featuredItems = [
    {
        name: "Rose must",
        price: "$45.50",
        description: "Delicate strawberry must",
        image: "images/coldcake.webp"
    },
    {
        name: "Red frute cake",
        price: "$5.00",
        description: "Classic delitefull frute cake",
        image: "images/frutecake3.web"
    },

    {
        name: "Red frute cake",
        price: "$5.00",
        description: "Classic delitefull frute cake",
        image: "images/frutecake3.web"
    },
    {
        name: "Red frute cake",
        price: "$5.00",
        description: "Classic delitefull frute cake",
        image: "images/frutecake3.web"
    },

    {
        name: "Red frute cake",
        price: "$5.00",
        description: "Classic delitefull frute cake",
        image: "images/frutecake3.webp"
    }    
    
];

function renderFeaturedItems(items) {
    const container = document.getElementById("featured-items");
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

console.log("Red Rose Dessert site loaded successfully");
