
document.getElementById("currentyear").textContent = new Date().getFullYear();

document.getElementById("LastModified").textContent = "Last Modified: " + document.lastModified;


const featuredItems = [
    {
        name: "Rose must",
        description: "Delicate strawberry must",
        image: "images/coldcake.webp",
        price: "$35"
       
    },
    {
        name: "Blueberry slice",
        description: "Blueberry slice with cream",
        image: "images/blueberry-slice2.webp",
        price: "$25"        
    },

    {
        name: "Personal gelly",
        description: "Personal gelly with fruits",
        image: "images/minigelly.webp",
        price: "$15"       
    },
    {
        name: "Vanilla cake",
        description: "Classic delitefull vanilla cake",
        image: "images/vanilla-slice.webp",
         price: "$25"       
    },

    {
        name: "Red frute cake",
        description: "Classic delitefull frute cake",
        image: "images/frutecake3.webp",
        price: "$30"        
    }    
    
];

function renderFeaturedItems(items) {
    const container = document.getElementById("featured-products");
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


