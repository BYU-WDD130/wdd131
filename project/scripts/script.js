document.getElementById("currentyear").textContent = new Date().getFullYear();

document.getElementById("LastModified").textContent = "Last Modified: " + document.lastModified;


// Product data array
const products = [
  { id: "cake", name: "3D Gelatin Cake" },
  { id: "cupcake", name: "Cupcake Box" },
  { id: "mousse", name: "Chocolate Mousse" },
  { id: "seasonal", name: "Seasonal Treat" }
];

// Populate select dropdown
const productSelect = document.getElementById("product");
products.forEach(product => {
  const option = document.createElement("option");
  option.value = product.id;
  option.textContent = product.name;
  productSelect.appendChild(option);
});

