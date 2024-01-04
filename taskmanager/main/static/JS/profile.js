function setUsernameFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username');
    const usernameElement = document.getElementById('username');

    if (usernameElement) {
        usernameElement.innerText = username;
    } else {
        console.error('Element with id "username" not found');
    }
}
const changePicButton = document.getElementById('change_pic_btn');
const profileImage = document.getElementById('profile-image');

changePicButton.addEventListener('click', () => {
    const imageUrl = prompt('Please enter the URL of the new profile picture:');

    if (imageUrl) {
        profileImage.src = imageUrl;
    }
});

document.addEventListener('DOMContentLoaded', setUsernameFromURL);

const sign_in_page_btn = document.getElementById('exit_btn');

sign_in_page_btn.addEventListener('click', () => {
    window.location.href = 'sign_in.html';
});

const sign_up_page_btn = document.getElementById('snippets_btn');

sign_up_page_btn.addEventListener('click', () => {
    window.location.href = 'home_page.html';
});