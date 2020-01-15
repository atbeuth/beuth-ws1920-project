function search() {
    let field = document.getElementById("search_text");
    let term = field.value;
    window.location.href = "/search/" + term;
    return false;
}

