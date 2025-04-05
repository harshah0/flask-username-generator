function copyUsername(id) {
    const username = document.getElementById(id).innerText;
    navigator.clipboard.writeText(username).then(() => {
        alert("Copied: " + username);
    }).catch(() => {
        alert("Copy failed.");
    });
}