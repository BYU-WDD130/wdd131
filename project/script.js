
document.getElementById("currentyear").textContent = new Date().getFullYear();




const featuredItems = [
    {
        name: "Rose Mousse",
        description: "Delicate strawberry mousse",
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
        description: "Personal jelly with fruits",
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
        name: "Jelly fruit cake",
        description: "Classic delightful fruit cake",
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


  const form = document.getElementById("subscribe-form");
  const modal = document.getElementById("confirmation-modal");
  const closeBtn = document.querySelector(".close-btn");

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(form);

    try {
      const response = await fetch(form.action, {
        method: form.method,
        body: formData,
        headers: { 'Accept': 'application/json' }
      });

      if (response.ok) {
        form.reset();
        modal.style.display = "block"; // Mostrar modal
      } else {
        alert("❌ Hubo un error. Intenta nuevamente.");
      }
    } catch (error) {
      alert("⚠️ Error de conexión. Intenta más tarde.");
    }
  });

  // Cerrar modal al hacer clic en la X
  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });

  // Cerrar modal si el usuario hace clic fuera del contenido
  window.addEventListener("click", (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });