function placeCaretAtEnd(el) {
  el.focus();
  if (typeof window.getSelection != "undefined" && typeof document.createRange != "undefined") {
    var range = document.createRange();
    range.selectNodeContents(el);
    range.collapse(false);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
  } else if (typeof document.body.createTextRange != "undefined") {
    var textRange = document.body.createTextRange();
    textRange.moveToElementText(el);
    textRange.collapse(false);
    textRange.select();
  }
}

(function() {
  (function($) {
    return $.widget("IKS.halloembedder", {
      options: {
        uuid: '',
        editable: null
      },
      populateToolbar: function(toolbar) {
        var button, widget;

        widget = this;

        getEnclosingEmbed = function() {
          var node;

          node = widget.options.editable.getSelection().commonAncestorContainer;
          return $(node).parents('div[data-embedtype="snippet"]').get(0);
        };

        button = $('<span></span>');
        button.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'Snippets',
          icon: 'icon-snippet',
          queryState: function(event) {
            var refreshedButton = button.hallobutton('checked', getEnclosingEmbed());
            if ($(refreshedButton).hasClass('ui-state-active')) {
              $(toolbar).find('button').not($(button).children()[0]).removeClass('ui-state-active');
            }
            return refreshedButton;
          }
        });
        button.addClass('action-types-list')
        toolbar.append(button);

        return button.on("click", function(event) {
          var enclosingLink, lastSelection;

          enclosingLink = getEnclosingEmbed();
          if (!enclosingLink) {

            lastSelection = widget.options.editable.getSelection();
            return ModalWorkflow({
              url: widget.options.modalUrl,
              onload: {
                'types-list': function(modal) {
                  $('div.snippet-list h2 a.snippet-embedder').click(function(event){
                    event.preventDefault();
                    modal.loadUrl(this.href);
                    return false;
                  });
                },
                'type-index': function(modal) {
                  $('div.snippet-list h2 a.snippet-choice').click(function(event){
                    event.preventDefault();
                    modal.loadUrl(this.href);
                    return false;
                  });
                },
                'choose_snippet': function(modal, jsonData) {
                  modal.respond('snippetChosen', jsonData['embed_html']);
                  modal.close();
                },
              },
              responses: {
                'snippetChosen': function(embedData) {
                  var elem = $(embedData).get(0);
                  lastSelection.insertNode(elem);
                  if (elem.getAttribute('contenteditable') === 'false') {
                    insertRichTextDeleteControl(elem);
                  }

                  var parentElement = $(lastSelection.endContainer);
                  var eol;
                  if ($(parentElement).is('[data-hallo-editor]')) {
                    eol = $(elem).parent().append("<br/>");
                  } else {
                    parentElement = $(parentElement).parent();
                    eol = $( "<br/>" ).insertAfter(parentElement);
                  }
                  placeCaretAtEnd(eol[0]);

                  return widget.options.editable.element.trigger('change');
                }
              }
            });
          }
        });
      }
    });
  })(jQuery);

}).call(this);