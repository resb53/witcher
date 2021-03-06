// Globals
var curtab = '';
var rstat = 0;

// Code for initialising the view
$(document).ready(function() {
  // Check if already complete, load background if not
  if ( ( lstat & 15 ) != 15 ) $("#base").attr("src","img/Riddler.png");
  else {
    $("#base").attr("src","img/Winner.png");
    $("#record_0").text("You're done, feel free to leave, and good luck!");
    $("#record_1").text('');
  }

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
          // Display response
          update_log(data['msg']);
          // Update visible tablets
          lstat = data['lstat'];
          hide_tabs(lstat);
          // Complete if finished
          if ( (data['lstat'] & 15) == 15) $("#base").attr("src","img/Winner.png");
        }
      });
    }
    else {
      update_log('Skeleton> Please have a tablet open before submitting a solution.');
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

  // Load text into tablets and show/hide solved tabs. Check for updates every 15 seconds
  load_riddles();
  // Refresh every 15 seconds. Report changes.
  setInterval(function() {
    load_riddles();
  }, 15000);

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

function load_riddles() {
  $.ajax({
    url: "getriddle",
    type: 'get',
    dataType: 'json',
    success: function(data) {
      // Fill each tabspan with their content -- response keys are span ids
      $(".tabspan").each( function() {
        $(this).html(data[$(this).attr('id')]);
      });
      if (rstat != data['rstat']) {
        update_log('The runes on the tablets shift from some external influence.');
        rstat = data['rstat'];
      }
    }
  });
}

function hide_tabs(lst) {
  // Cyan
  if ( (lst & 8) == 8 ) $('#cyan').hide();
  else $('#cyan').show();
  // Violet
  if ( (lst & 4) == 4 ) $('#violet').hide();
  else $('#violet').show();
  // Purple
  if ( (lst & 2) == 2 ) $('#purple').hide();
  else $('#purple').show();
  // Red
  if ( (lst & 1) == 1 ) $('#red').hide();
  else $('#red').show();
}
