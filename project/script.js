
document.getElementById("currentyear").textContent = new Date().getFullYear();




const featuredItems = [
    {
        name: "Rose Mousse",
        description: "Delicate strawberry must",
        image: "images/coldcake.webp",
        price: ""
       
    },
    {
        name: "Blueberry slice",
        description: "Blueberry slice with cream",
        image: "images/blueberry-slice2.webp",
        price: ""        
    },

    {
        name: "Personal gelly",
        description: "Personal gelly with fruits",
        image: "images/minigelly.webp",
        price: ""       
    },
    {
        name: "Vanilla cake",
        description: "Classic delitefull vanilla cake",
        image: "images/vanilla-slice.webp",
         price: ""       
    },

    {
        name: "Red frute cake",
        description: "Classic delitefull frute cake",
        image: "images/frutecake3.webp",
        price: ""        
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

  const video = document.getElementById('video1');
  const btn = document.getElementById('playBtn');

  btn.addEventListener('click', () => {
    video.play();
  });
