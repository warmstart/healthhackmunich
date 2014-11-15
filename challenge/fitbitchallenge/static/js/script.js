(function($, undefined){

  $(function(){
    $.material.init();

    $('#login').click(function(){
      $('.marketing-text').addClass('fadeOutLeft');

      setTimeout(function(){
        $('.login-box').addClass('fadeInRight');
      }, 240);

    });
  });


})(window.jQuery);