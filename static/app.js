$(document).ready(function() {
  $('.hoverkins').tooltipster({
    theme: 'tooltipster-light'
  });
  $('#submit-div').hide();
  $('#view-div').hide();
  $('#submit-button').click(function() {
    $('.buttons').addClass('tip-top');
    $('#submit-div').show();
    $('#view-div').hide();
  });
  $('#view-button').click(function() {
    $('.buttons').addClass('tip-top');
    $('#view-div').show();
    $('#submit-div').hide();
    $('.alert').hide();
  });

  // this may just be my greatest accomplishment ever
  $("#filter").keyup(function(){
    var filter = $(this).val(), count=0;
    $("#accordion .card").each(function(){
      if ($(this).text().search(new RegExp(filter, "i")) < 0) {
        $(this).fadeOut();
      } else {
        $(this).show();
        count ++;
      }
      if(filter=='') {
        $("#filter-count").hide();
      }
    });
    var numberItems = count;
    if(count==0) {
      $("#filter-count").show().text("Nothing found ¯\\_(ツ)_/¯");
    }
  });
});
