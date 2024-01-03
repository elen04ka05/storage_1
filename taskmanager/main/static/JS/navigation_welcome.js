const signUpBtn = document.getElementById('sign_up');
const signInBtn = document.getElementById('sign_in');

signUpBtn.addEventListener('click', () => {
    window.location.href = 'sign_up.html';
});

signInBtn.addEventListener('click', () => {
    window.location.href = 'sign_in.html';
});