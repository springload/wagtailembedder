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
        toolbar.append(button);
        return button.on("click", function(event) {
          var enclosingLink, insertionPoint, lastSelection;

          enclosingLink = getEnclosingEmbed();
          if (!enclosingLink) {

            lastSelection = widget.options.editable.getSelection();
            insertionPoint = $(lastSelection.endContainer).parentsUntil('.richtext').last();
            return ModalWorkflow({
              url: window.embedderChooserUrls.embedderChooser,
              responses: {
                snippetChosen: function(embedData) {
                  var elem = $(embedData).get(0);
                  lastSelection.insertNode(elem);
                  if (elem.getAttribute('contenteditable') === 'false') {
                    insertRichTextDeleteControl(elem);
                  }
           
                  var parentElement = $(lastSelection.endContainer);
                  var eol;
                  if ($(parentElement).hasClass('richtext')) {
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