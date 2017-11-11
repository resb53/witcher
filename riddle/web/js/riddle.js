// Code for initialising the view
$(document).ready(function() {
  $("#view").attr("src","img/init.jpg");
  // Prepare action when text submitted
  $("#query").on("submit", function(e) {
    e.preventDefault();
    // Loop through output lines, updating them
    new_text = '> ' + $("#solution").val();
    $("#solution").val('');
    old_text = '';
    for (i=0; i<10; i++) {
      old_text = $("#record_"+i).text();
      $("#record_"+i).text(new_text);
      new_text = old_text;
    }
  });
});
