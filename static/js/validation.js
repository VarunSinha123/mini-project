// static/js/validation.js
function validateForm(form) {
    const inputs = form.querySelectorAll('input, select, textarea');
    let isValid = true;

    inputs.forEach(input => {
        // Remove previous error messages
        const existingError = input.nextElementSibling;
        if (existingError && existingError.classList.contains('error-message')) {
            existingError.remove();
        }

        // Validation checks
        if (input.hasAttribute('required') && !input.value.trim()) {
            displayError(input, 'This field is required');
            isValid = false;
        }

        // Email validation
        if (input.type === 'email') {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(input.value)) {
                displayError(input, 'Please enter a valid email address');
                isValid = false;
            }
        }

        // Password strength
        if (input.id === 'password') {
            if (input.value.length < 8) {
                displayError(input, 'Password must be at least 8 characters');
                isValid = false;
            }
        }
    });

    return isValid;
}

function displayError(input, message) {
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.style.color = 'red';
    errorElement.style.fontSize = '0.8em';
    errorElement.textContent = message;
    input.after(errorElement);
}

document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            if (!validateForm(form)) {
                e.preventDefault();
            }
        });
    });
});