function validateLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");

    if (username === "user" && password === "password") {
        alert("Login successful!");
        return true;
    } else {
        errorMessage.textContent = "Invalid username or password.";
        return false;
    }
}