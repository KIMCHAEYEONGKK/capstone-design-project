
    jQuery(document).ready(function(){
      /*   $('.tabmenu li>a').mouseeover(function(){
            $('#modal_1').addClass('active');
        });
        $('.mobtn_1').mouseout(function(){
            $('#modal_1').removeClass('active');
        });
 */
        $(function(){
            $('.section_3>.tabmenu>li>a').click(function(){
                $(this).parent().addClass('active')
                .siblings()
                .removeClass('active')
                return false;
            });
        });

    });
