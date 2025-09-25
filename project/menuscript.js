
document.getElementById("currentyear").textContent = new Date().getFullYear();



const featuredItems = [
  {
    name: "3D Rose Gelatin Cake",
    category: "jelly",
    price: "",
    image: "images/3djelly.webp",
   },
  {
    name: "Strawberry Mousse",
    category: "mousse",
    price: "",
    image: "images/coldcake.webp",  

  },
  {
    name: "Special dad cake",
    category: "cake",
    price: "",
    image: "images/dadcake2.webp",

  },
  {
    name: "Vanilla cake",
    category: "cake",
    price: "",
    image: "images/vanilla-slice.webp",
  },
  {
    name: "Chocolate and flan Cake",
    category: "cake",
    price: "",
    image: "images/chocoflan5.webp",
  },
  {
    name: "Classic Semita Cookies",
    category: "cookie",
    price: "",
    image: "images/semita2.webp",
  },
  {
    name: "Pineapple jelly",
    category: "jelly",
    price: "",
    image: "images/pineaplecake.webp",
  },
  {
    name: "Passion Fruit Mousse",
    category: "mousse",
    price: "",
    image: "images/passionfrute.webp",
  },
    {
    name: "Jelly with fruits",
    category: "jelly",
    price: "",
    image: "images/jellycake4.webp",
  },
      {
    name: "Jelly customized",
    category: "jelly",
    price: "",
    image: "images/jellycake3.webp",
  },
      {
    name: "Jelly garden",
    category: "jelly",
    price: "",
    image: "images/jellycake5.webp",
  },
      {
    name: "Mini Jelly",
    category: "jelly",
    price: "",
    image: "images/jellycake6.webp",
  },
     {
    name: "Chocolate cake",
    category: "cake",
    price: "",
    size: "6 inch",
    image: "images/chocolatecake.webp",
  },

     {
    name: "Birthday cake",
    category: "cake",
    price: "",
    size: "8 inch",
    image: "images/birthdaycake.webp",
  },

       {
    name: "Strawberry and cream cake",
    category: "cake",
    price: "",
    size: "6 inch",
    image: "images/whitecake.webp",
  },

         {
    name: "vintage cake",
    category: "cake",
    price: "",
    size: "6 inch",
    image: "images/vintagecake.webp",
  },

         {
    name: "Jelly with fruits",
    category: "jelly",
    price: "",
    size: "6 inch",
    image: "images/jelly1.webp",
  },  

           {
    name: "Cupcake",
    category: "cupcake",
    price: "",
    size: "6 inch",
    image: "images/copcake.webp",
  },  

           {
    name: "chocofan frutal",
    category: "cake",
    price: "",
    size: "6 inch",
    image: "images/frutal.webp",
  },

             {
    name: "Cupcake",
    category: "cupcake",
    price: "",
    size: "6 inch",
    image: "images/chocopcake.webp",
  },

               {
    name: "mini cake",
    category: "cake",
    price: "",
    image: "images/bluecake.webp",
  },

                 {
    name: "choflan frutal",
    category: "cake",
    price: "",
    image: "images/chocoflanfrute.webp",
  },

                 {
    name: "Red velvet cake",
    category: "cake",
    price: "",
    image: "images/redvelvet.webp",
  },

                 {
    name: "vanilla and chocolate cake",
    category: "cake",
    price: "",
    image: "images/dasilva.webp",
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

const nav = document.querySelector("#mobileMenu");
const abrir = document.querySelector("#abrir");
const cerrar = document.querySelector("#cerrar");

abrir.addEventListener("click", () => nav.classList.add("visible"));

cerrar.addEventListener("click", () => nav.classList.remove("visible"));
});

