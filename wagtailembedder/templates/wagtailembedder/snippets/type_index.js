function(modal) {
    $('div.snippet-list h2 a.snippet-choice').click(function(event){
        event.preventDefault();
        modal.loadUrl(this.href);
        // $.get($(this).attr('href'), function(response) {
            
        // })
        // .done(function() {
        //     console.log( "second success" );
        // })
        // .fail(function(error) {
        //     console.log(error);
        //     console.log( "error" );
        // });

        return false;
    });
}