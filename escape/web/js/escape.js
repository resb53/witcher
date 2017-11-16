// Code for initialising the view
$(document).ready(function() {
  $("#view").attr("src","img/Room.png");

  // Prepare action when text submitted
  $("#query").on("submit", function(e) {
    e.preventDefault();
    // Prepare to loop through output lines, updating them
    comsubmit = $("#command").val();
    update_log('> ' + comsubmit);
    // Reset input field
    $("#command").val('');
    // Prepare form
    dataform = {};
    dataform['command'] = comsubmit;
    // Submit solution
    $.ajax({
      url: '/query',
      type: 'post',
      dataType: 'json',
      data: dataform,
      success: function(data) {
        // Display response
        update_log(data['msg']);
        if (data['complete']) {
          update_log(data['complete'])
        }
      }
    });
  });

  // Handle text bar when empty / focussed / etc.
  $("#command").focus( function(e) {
    if ($(this).is(".empty")) {
      // Remove this class, and empty the field
      $(this).val('').removeClass('empty');
    }
  });
  $("#command").blur( function(e) {
    if ($(this).val() == '' && $(this).not(".empty")) {
      $(this).val('Enter solutions here...').addClass('empty');
    }
  });
});

function update_log(newval) {
  new_text = newval;
  old_text = '';
  for (i=0; i<20; i++) {
    old_text = $("#record_"+i).html();
    $("#record_"+i).html(new_text);
    new_text = old_text;
  }
}
