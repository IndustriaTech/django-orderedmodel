/*
Code taken from django snippets
http://djangosnippets.org/snippets/1053/
*/
(function($){
    $(function() {
        $('div.inline-group').sortable({
            items: 'div.inline-related',
            handle: 'h3:first',
            update: function() {
                $(this).find('div.inline-related').each(function(i) {
                    if ($(this).find('input[id$="-id"]').val()) {
                        $(this).find('input[id$=order]').val(i+1);
                    }
                });
            },

            // Dirty hack for not loosing value of selects while mooving
            start: function(evt, ui) {
                ui.item.find('select').each(function(){
                    $(this).data('value', $(this).val());
                });
            },
            stop: function(evt, ui) {
                ui.item.find('select').each(function(){
                    $(this).val($(this).data('value'));
                });
            }
        });
        $('div.inline-related h3').css('cursor', 'move');
        $('div.inline-related').find('input[id$=order]').parent('div').hide();
    });
})(jQuery);