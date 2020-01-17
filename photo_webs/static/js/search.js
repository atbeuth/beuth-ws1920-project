function search() {
    let field = document.getElementById("search_text");
    let term = field.value;
    if (term.replace(/\s/g,'') != '')
        window.location.href = "/search/" + term;
    return false;
}

