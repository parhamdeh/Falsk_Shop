document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    form.addEventListener("submit", (event) => {
        const username = form.querySelector("input[name='username']").value;
        if (username.length < 3) {
            alert("نام کاربری باید حداقل ۳ کاراکتر باشد!");
            event.preventDefault(); // جلوگیری از ارسال فرم
        }
    });
});
