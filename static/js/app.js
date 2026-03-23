const form = document.getElementById("loginForm");
const message = document.getElementById("message");

if (form) {
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
      message.textContent = "Both fields are required.";
      return;
    }

    message.textContent = "Access denied. You are not the Dragon Warrior.";
  });
}