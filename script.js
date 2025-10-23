// 🧾 Simple JS Functions for Validation and Alerts

function validateLogin() {
  const username = document.querySelector('input[name="username"]').value.trim();
  const password = document.querySelector('input[name="password"]').value.trim();

  if (username === "" || password === "") {
    alert("Please enter both username and password!");
    return false;
  }
  return true;
}

function validateBooking() {
  const name = document.querySelector('input[name="name"]').value.trim();
  const seats = document.querySelector('input[name="seats"]').value.trim();
  const from = document.querySelector('input[name="from_place"]').value.trim();
  const to = document.querySelector('input[name="to_place"]').value.trim();

  if (!name || !seats || !from || !to) {
    alert("Please fill all booking details!");
    return false;
  }

  alert("✅ Booking details submitted successfully!");
  return true;
}

// 🌈 Simple Animation Effect
document.addEventListener("DOMContentLoaded", () => {
  const container = document.querySelector(".container");
  if (container) {
    container.style.opacity = 0;
    setTimeout(() => {
      container.style.transition = "opacity 1s";
      container.style.opacity = 1;
    }, 100);
  }
});
