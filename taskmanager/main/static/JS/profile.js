function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function setUsernameFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const username = urlParams.get('username');
    const usernameElement = document.getElementById('username');

    if (usernameElement) {
        usernameElement.innerText = (username || usernameElement.dataset.username || "ZAEBALAS");
    } else {
        console.error('Element with id "username" not found');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    setUsernameFromURL();

    const editBtn = document.getElementById('edit_btn');

    // Добавим только для отладки
    console.log("Username element:", document.getElementById('username'));
    console.log("Username from URL parameter:", new URLSearchParams(window.location.search).get('username'));

    editBtn.addEventListener('click', () => {
        const usernameElement = document.getElementById('username');
        const newUsername = (usernameElement.textContent || usernameElement.innerText).trim();

        if (editBtn.innerText.toLowerCase() === 'save') {
            fetch('update_username.html', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ new_username: newUsername }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Username updated successfully!');
                    editBtn.innerText = 'Edit';
                    usernameElement.removeAttribute('contenteditable');
                } else {
                    alert('Failed to update username');
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        } else {
            usernameElement.setAttribute('contenteditable', true);
            usernameElement.focus();
            editBtn.innerText = 'Save';
        }
    });
});

const exitBtn = document.getElementById('exit_btn');

exitBtn.addEventListener('click', () => {
    window.location.href = 'sign_in.html';
});