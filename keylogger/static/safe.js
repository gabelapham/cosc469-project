document.getElementById('trustButton').addEventListener('click', function() {
    alert("Thanks for trusting us! Your data is now totally safe and secure. Wink wink.");
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loginButton').addEventListener('click', function() {
        window.location.href = "http://127.0.0.1:5500/keylogger/pages/login.html";
    });
});