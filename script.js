document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        phone: document.getElementById('phone').value,
        age: document.getElementById('age').value,
        height: document.getElementById('height').value,
        gender: document.getElementById('gender').value
    };

    // You can handle form data here (e.g., send to a server or display it)
    console.log('Form Data:', formData);

    alert('Registration successful!');
});
