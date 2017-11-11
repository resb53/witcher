// Code for initialising the view
$(document).ready(function() {
  $("#base").attr("src","img/Riddler.png");

  // Prepare action when text submitted
  $("#query").on("submit", function(e) {
    e.preventDefault();
    // Submit solution
    new_text = '> ' + $("#solution").val();
    $.ajax({
      url: '/query',
      type: 'post',
      dataType: 'json',
      data: $("#query").serialize(),
      success: function(data) {
        update_log(data['msg']);
      }
    });
    // Reset input field
    $("#solution").val('');
    // Prepare to loop through output lines, updating them
    update_log(new_text);
  });

  // Handle text bar when empty / focussed / etc.
  $("#solution").focus( function(e) {
    if ($(this).is(".empty")) {
      // Remove this class, and empty the field
      $(this).val('').removeClass('empty');
    }
  });
  $("#solution").blur( function(e) {
    if ($(this).val() == '' && $(this).not(".empty")) {
      $(this).val('Enter solutions here...').addClass('empty');
    }
  });
});

function update_log(newval) {
  new_text = newval;
  old_text = '';
  for (i=0; i<10; i++) {
    old_text = $("#record_"+i).text();
    $("#record_"+i).text(new_text);
    new_text = old_text;
  }
}
