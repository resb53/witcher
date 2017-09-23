// Code for navigating the maze and interacting with the website
$(document).ready(function() {
  $("#view").attr("src","img/" + loc["zone"] + "/" + loc["image"] + "?t=" + loc["tile"] + loc["face"]);
  populateArrows();
});

// Catch movement keypresses
var navok = true;

$(window).keypress(function(e) {
  if (navok && (e.which == 87 || e.which == 119)) {
    if (loc["allowed"].indexOf('w') >= 0) {
      navok = false;
      navigate("w")
    }
  }
  if (navok && (e.which == 65 || e.which == 97)) {
    if (loc["allowed"].indexOf('a') >= 0) {
      navok = false;
      navigate("a")
    }
  }
  if (navok && (e.which == 83 || e.which == 115)) {
    if (loc["allowed"].indexOf('s') >= 0) {
      navok = false;
      navigate("s")
    }
  }
  if (navok && (e.which == 68 || e.which == 100)) {
    if (loc["allowed"].indexOf('d') >= 0) {
      navok = false;
      navigate("d")
    }
  }
  if (navok && (e.which == 32)) {
    if (loc["allowed"].indexOf('action') >= 0) {
      // Do stuff
    }
  }
});

// Carry out a user action
var navigate = function(a) {
  $.getJSON("navigate?a=" + a, function(data) {
    loc = data
    $("#view").fadeTo(250, 0.7, function() {
      $("#view").attr("src","img/" + loc["zone"] + "/" + loc["image"] + "?t=" + loc["tile"] + loc["face"]).fadeTo(250, 1);
      populateArrows();
      navok = true;
    });
  });
};

// Show relevant arrows
var populateArrows = function() {
  if (loc["allowed"].indexOf('w') >= 0) {
    $("#st").attr("src","img/Straight.png");
  }
  else {
    $("#st").attr("src","img/StraightW.png");
  }
  if (loc["allowed"].indexOf('a') >= 0) {
    $("#lt").attr("src","img/Left.png");
  }
  else {
    $("#lt").attr("src","img/LeftW.png");
  }
  if (loc["allowed"].indexOf('d') >= 0) {
    $("#rt").attr("src","img/Right.png");
  }
  else {
    $("#rt").attr("src","img/RightW.png");
  }
};
