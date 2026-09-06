document.querySelectorAll('.form-message').forEach((message) => {
    window.setTimeout(() => {
        message.classList.add('is-hiding');

        window.setTimeout(() => message.remove(), 350);
    }, 4000);
});
