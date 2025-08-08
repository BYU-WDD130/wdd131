
document.getElementById("currentyear").textContent = new Date().getFullYear();

document.getElementById("LastModified").textContent = "Last Modified: " + document.lastModified;


const featuredItems = [
    {
        name: "Rose must",
        price: "",
        description: "Delicate strawberry must",
        image: "images/coldcake.webp"
    },
    {
        name: "Blueberry slice",
        price: "",
        description: "Blueberry slice with cream",
        image: "images/blueberry-slice2.webp"
    },

    {
        name: "Personal gelly",
        price: "",
        description: "Personal gelly with fruits",
        image: "images/minigelly.webp"
    },
    {
        name: "Vanilla cake",
        price: "",
        description: "Classic delitefull vanilla cake",
        image: "images/vanilla-slice.webp"
    },

    {
        name: "Red frute cake",
        price: "",
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

