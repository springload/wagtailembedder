(function() {
  (function($) {
    return $.widget("IKS.halloembedder", {
      options: {
        uuid: '',
        editable: null
      },
      populateToolbar: function(toolbar) {
        var button, getEnclosingLink, widget;

        widget = this;
        getEnclosingLink = function() {
          var node;

          node = widget.options.editable.getSelection().commonAncestorContainer;
          return $(node).parents('a').get(0);
        };
        button = $('<span></span>');
        button.hallobutton({
          uuid: this.options.uuid,
          editable: this.options.editable,
          label: 'Snippets',
          icon: 'icon-snippet',
          command: null
          /*queryState: function(event) {
            return button.hallobutton('checked', !!getEnclosingLink());
          }*/
        });
        toolbar.append(button);
        return button.on("click", function(event) {
          var enclosingLink, lastSelection, url;
          url = window.embedderChooserUrls.embedderChooser

          return ModalWorkflow({
              url: url,
              responses: {
                snippetClassChosen: function(pageData) {
                  console.log(pageData);
                },
                snippetObjectChosen: function(pageData) {
                  var a;

                  a = document.createElement('a');
                  a.setAttribute('href', pageData.url);
                  if (pageData.id) {
                    a.setAttribute('data-id', pageData.id);
                    a.setAttribute('data-linktype', 'page');
                  }
                  if ((!lastSelection.collapsed) && lastSelection.canSurroundContents()) {
                    lastSelection.surroundContents(a);
                  } else {
                    a.appendChild(document.createTextNode(pageData.title));
                    lastSelection.insertNode(a);
                  }
                  return widget.options.editable.element.trigger('change');
                }
              }
            });
          // enclosingLink = getEnclosingLink();
          /*if (enclosingLink) {
            $(enclosingLink).replaceWith(enclosingLink.innerHTML);
            button.hallobutton('checked', false);
            return widget.options.editable.element.trigger('change');
          } else {
            lastSelection = widget.options.editable.getSelection();
            if (lastSelection.collapsed) {
              url = window.chooserUrls.pageChooser + '?allow_external_link=true&allow_email_link=true&prompt_for_link_text=true';
            } else {
              url = window.chooserUrls.pageChooser + '?allow_external_link=true&allow_email_link=true';
            }
            return ModalWorkflow({
              url: url,
              responses: {
                pageChosen: function(pageData) {
                  var a;

                  a = document.createElement('a');
                  a.setAttribute('href', pageData.url);
                  if (pageData.id) {
                    a.setAttribute('data-id', pageData.id);
                    a.setAttribute('data-linktype', 'page');
                  }
                  if ((!lastSelection.collapsed) && lastSelection.canSurroundContents()) {
                    lastSelection.surroundContents(a);
                  } else {
                    a.appendChild(document.createTextNode(pageData.title));
                    lastSelection.insertNode(a);
                  }
                  return widget.options.editable.element.trigger('change');
                }
              }
            });
          }*/
        });
      }
    });
  })(jQuery);

}).call(this);