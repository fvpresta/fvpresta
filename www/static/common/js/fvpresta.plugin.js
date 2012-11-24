/* Vertical align v1.0
   Create by tronghieu.ha@gmail.com */

(function($){
    $.fn.vAlign = function() {
        var obj = $(this);

        if (obj.is('img')) {
            /* Because the images are not completly loaded on document ready (just the tag img but not image itseft)
               and thus we will get 0 if we use obj.height() on document ready
               So we need to wait for image finishing loading in case of object is image
            */
            obj.load(function() {
                processAlign($(this));
            });

        } else {
            processAlign($(this));
        }

        // Align function
        processAlign = function(obj) {
            // calculate the new padding and height
            var childHeight = obj.height();
            var parentHeight = obj.parent().height();
            var diff = Math.round( ( (parentHeight - childHeight) / 2) );
            // apply new values
            obj.css( { "display": "block", "margin-top": diff } );
        }
    }
})(jQuery);