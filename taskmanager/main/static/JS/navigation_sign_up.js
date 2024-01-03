document.addEventListener('DOMContentLoaded', () => {
    const signUpForm = document.getElementById('signup-form');

    function registerUser(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        const username = document.getElementById('username').value;
        const queryString = "?username=" + username;
        window.location.href = "profile.html" + queryString;
    }

    signUpForm.addEventListener('submit', registerUser); // Register the registerUser function for form submission
});

const sign_up_page_btn = document.getElementById('sign_in_page_btn');

sign_up_page_btn.addEventListener('click', () => {
    window.location.href = 'sign_in.html';
});