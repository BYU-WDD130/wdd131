// Parse query string and display data
function getQueryData() {
  const params = new URLSearchParams(window.location.search);
  return {
    fullName: params.get("fullName"),
    email: params.get("email"),
    pickupDate: params.get("pickupDate"),
    product: params.get("product"),
    flavor: params.get("flavor"),
    extras: params.getAll("extras"),
    notes: params.get("notes")
  };
}

function displayReview(data) {
  const section = document.getElementById("reviewContent");
  section.innerHTML = `
    <h2>Order Summary</h2>
    <ul>
      <li><strong>Name:</strong> ${data.fullName}</li>
      <li><strong>Email:</strong> ${data.email}</li>
      <li><strong>Pickup Date:</strong> ${data.pickupDate}</li>
      <li><strong>Product:</strong> ${data.product}</li>
      <li><strong>Flavor:</strong> ${data.flavor}</li>
      <li><strong>Extras:</strong> ${data.extras.length > 0 ? data.extras.join(", ") : "None"}</li>
      <li><strong>Notes:</strong> ${data.notes || "None"}</li>
    </ul>
  `;
}

// LocalStorage counter
function incrementCounter() {
  let count = localStorage.getItem("reviewCount");
  count = count ? parseInt(count) + 1 : 1;
  localStorage.setItem("reviewCount", count);
  document.getElementById("reviewCount").textContent = count;
}

// Initialize on load
document.addEventListener("DOMContentLoaded", () => {
  const formData = getQueryData();
  displayReview(formData);
  incrementCounter();
});