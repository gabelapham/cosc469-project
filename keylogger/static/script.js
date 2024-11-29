// script.js
document.getElementById('submitBtn').addEventListener('click', () => {
    // Get input values
    const name = document.getElementById('name').value;
    const account = document.getElementById('account').value;
    const balance = document.getElementById('balance').value;
    
    // Validate inputs
    if (name === '' || account === '' || balance === '') {
        alert('Please fill out all fields!');
        return;
    }

    // Update output section
    document.getElementById('outputName').textContent = name;
    document.getElementById('outputAccount').textContent = account;
    document.getElementById('outputBalance').textContent = `$${parseFloat(balance).toFixed(2)}`;

    // Clear form
    document.getElementById('bankForm').reset();
});
