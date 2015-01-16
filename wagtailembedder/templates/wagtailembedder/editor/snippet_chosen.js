function(modal) {
    modal.respond('snippetChosen', '{{ embed_html|escapejs }}');
    modal.close();
}