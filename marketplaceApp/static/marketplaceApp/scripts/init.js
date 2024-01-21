/* var carousels = document.getElementsByClassName("carousel");
var materialboxes = document.getElementsByClassName("materialboxed");

function hidefunction(){
  for (var i = 0; i < carousels.length; i++) {
    carousels.item(i).style.opacity = "0.0";
  }
   for (var i = 0; i < materialboxes.length; i++) {
    materialboxes.item(i).style.opacity = "1.0";
  }
}

function showfunction() {
  for (var i = 0; i < carousels.length; i++) {
    carousels.item(i).style.opacity = "1.0";
  }
} */

(function($){
  $(function(){

    $(document).ready(function(){
      $('.carousel').carousel({
        duration: 100,
        dist: -50,
        spacing: 2,
      });
/*       $('.materialboxed').materialbox({
        onOpenEnd: hidefunction,
        onCloseEnd: showfunction,
      }); */
    });

  }); // end of document ready
})(jQuery); // end of jQuery name space