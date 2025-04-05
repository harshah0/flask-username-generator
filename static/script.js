function copyUsername(id) {
    const username = document.getElementById(id).innerText;
    navigator.clipboard.writeText(username).then(() => {
        alert("Copied: " + username);
    }).catch(() => {
        alert("Copy failed.");
    });
}

// Dark mode toggle
document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("modeToggle");
    toggle.addEventListener("change", function () {
        document.body.classList.toggle("dark-mode");
    });
});
