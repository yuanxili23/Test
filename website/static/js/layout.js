var error_handler = function (error) {
    if (error.status == 400) {
        window.location = "error/400.html";
    } else if (error.status == 401) {
        window.location = "error/401.html";
    } else if (error.status == 403) {
        window.location = "error/403.html";
    } else if (error.status == 404) {
        window.location = "error/404.html";
    } else if (error.status == 405) {
        window.location = "error/405.html";
    } else if (error.status == 409) {
        window.location = "error/409.html";
    } else {
        window.location = "error/unknown.html";
    }
}