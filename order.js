// order.js

document.addEventListener("DOMContentLoaded", () => {
  const nameField = document.getElementById("name");
  const emailField = document.getElementById("email");

  // Load stored name and email if available
  if (localStorage.getItem("rrd_name")) {
    nameField.value = localStorage.getItem("rrd_name");
  }
  if (localStorage.getItem("rrd_email")) {
    emailField.value = localStorage.getItem("rrd_email");
  }

  const form = document.getElementById("orderForm");
  const feedback = document.getElementById("feedback");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const name = nameField.value.trim();
    const email = emailField.value.trim();
    const date = document.getElementById("date").value;
    const dessert = document.getElementById("dessert").value;

    if (!name || !email || !date || !dessert) {
      alert("Please complete all required fields.");
      return;
    }

    // Store name and email for future visits
    localStorage.setItem("rrd_name", name);
    localStorage.setItem("rrd_email", email);

    // Simulate successful submission
    form.reset();
    feedback.style.display = "block";

    setTimeout(() => {
      feedback.style.display = "none";
    }, 5000);
  });
});