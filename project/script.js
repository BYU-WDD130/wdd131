const featuredItems = [
    {
        name: "Rose Macarons",
        price: "$3.50",
        description: "Delicate rose-flavored almond cookies",
        image: "images/macarons.jpg"
    },
    {
        name: "Red Velvet Slice",
        price: "$5.00",
        description: "Classic red velvet cake with cream cheese frosting",
        image: "images/redvelvet.jpg"
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
