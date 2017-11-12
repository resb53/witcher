// Globals
var curtab = ''
var rstat = 0;

// Code for initialising the view
$(document).ready(function() {
  $("#base").attr("src","img/Riddler.png");

  // Prepare action when text submitted
  $("#query").on("submit", function(e) {
    e.preventDefault();
    // Prepare to loop through output lines, updating them
    solsubmit = $("#solution").val();
    update_log('You> ' + solsubmit);
    // Reset input field
    $("#solution").val('');
    // Prepare form
    //dataform = $("#query").serialize();
    if (curtab) {
      dataform = {};
      dataform['riddle'] = curtab;
      dataform['solution'] = solsubmit;
      // Submit solution
      $.ajax({
        url: '/query',
        type: 'post',
        dataType: 'json',
        data: dataform,
        success: function(data) {
          update_log(data['msg']);
        }
      });
    }
    else {
      update_log('Please have a tablet open before submitting a solution.');
    }
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

  // Load text into tablets
  load_riddles(rstat);
  
  // Handle clicks on tablets
  $(".tablet").click( function(e) {
    //update_log($(this).attr('id') + ' clicked.');
    tab = '#' + $(this).attr('id') + 'tab';
    // As a precaution, close any open tab
    if (curtab) {
      $(curtab).hide();
    }
    $(tab).show();
    curtab = tab;
  });

  // Handled tablet closeicons
  $(".closeicon").click( function(e) {
    $(curtab).hide();
    curtab = '';
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

function load_riddles(s) {
  $.ajax({
    url: "getriddle?r=" + s,
    type: 'get',
    dataType: 'json',
    success: function(data) {
      // Fill each tabspan with their content -- response keys are span ids
      $(".tabspan").each( function() {
        $(this).html(data[$(this).attr('id')]);
      });
    }
  });
}
