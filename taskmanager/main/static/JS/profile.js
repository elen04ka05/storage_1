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

document.addEventListener('DOMContentLoaded', function() {
    setUsernameFromURL();
    const usernameElement = document.getElementById('username');
    const usernameFromData = usernameElement.dataset.username;

    if (usernameElement.innerText.trim() === "") {
        usernameElement.innerText = (usernameFromData !== '') ? usernameFromData : "ZAEBALAS";
    }

    const changePicButton = document.getElementById('change_pic_btn');
    const profileImage = document.getElementById('profile-image');

    changePicButton.addEventListener('click', () => {
        const imageUrl = prompt('Please enter the URL of the new profile picture:');

        if (imageUrl) {
            profileImage.src = imageUrl;
        }
    });

    const sign_up_page_btn = document.getElementById('exit_btn');

    sign_up_page_btn.addEventListener('click', () => {
        window.location.href = 'sign_in.html';
    });

    const editBtn = document.getElementById('edit_btn');
    let isEditing = false;

    editBtn.addEventListener('click', () => {
        if (!isEditing) {
            usernameElement.setAttribute('contenteditable', true);
            usernameElement.focus();
            editBtn.innerText = 'Save';
            isEditing = true;
        } else {
            usernameElement.removeAttribute('contenteditable');
            editBtn.innerText = 'Edit';
            isEditing = false;
        }
    });

    usernameElement.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            usernameElement.blur();
            if (isEditing) {
                editBtn.dispatchEvent(new Event('click'));
            }
        }
    });
});