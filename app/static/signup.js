document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    form.addEventListener("submit", (event) => {
        const password = form.querySelector("input[name='password']").value;
        if (password.length < 8) {
            alert("رمز عبور باید حداقل ۸ کاراکتر باشد!");
            event.preventDefault();
        }
    });
});
