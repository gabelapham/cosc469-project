document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('loginForm').addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent the default form submission
        window.location.href = 'bank2.html'; // Redirect to banking2.html
    });
});