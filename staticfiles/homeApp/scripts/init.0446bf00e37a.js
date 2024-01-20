(function($){
  $(function(){

    $('.sidenav').sidenav();

    $(document).ready(function(){
      $('select').formSelect();
    });

    $(document).ready(function(){
      $('.timepicker').timepicker();
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space