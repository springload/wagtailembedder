function(modal) {
    $('div.snippet-list h2 a.snippet-embedder').click(function(event){
        event.preventDefault();
        modal.loadUrl(this.href);
        return false;
    });
}