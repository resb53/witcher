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
      navigate("w");
    }
  }
  if (navok && (e.which == 65 || e.which == 97)) {
    if (loc["allowed"].indexOf('a') >= 0) {
      navigate("a");
    }
  }
  if (navok && (e.which == 83 || e.which == 115)) {
    if (loc["allowed"].indexOf('s') >= 0) {
      navigate("s");
    }
  }
  if (navok && (e.which == 68 || e.which == 100)) {
    if (loc["allowed"].indexOf('d') >= 0) {
      navigate("d");
    }
  }
  if (navok && (e.which == 32)) {
    if (loc["allowed"].indexOf('action') >= 0) {
      doAction();
    }
  }
});

// Carry out a user movement
var navigate = function(a) {
  navok = false;
  $.getJSON("navigate?a=" + a + "&t=" + loc["tile"] + loc["face"], function(data) {
    loc = data
    $("#view").fadeTo(250, 0.7, function() {
      $("#view").attr("src","img/" + loc["zone"] + "/" + loc["image"]).fadeTo(250, 1);
      // Move on the map
      $("#you").css('left',loc["left"]);
      $("#you").css('top',loc["top"]);
      // Check rstat
      if (loc["rstat"] > 0) {
        $("#map").show();
        if (loc["rstat"] == 2) $("#minimap").attr("src","img/mape.png");
        if (loc["rstat"] == 3) $("#minimap").attr("src","img/mapf.png");
      }
      // Draw arrows
      populateArrows();
      navok = true;
    });
  });
};

// Show relevant arrows
var populateArrows = function() {
  if (loc["allowed"].indexOf('action') >= 0) {
    $("#st").attr("src","img/Action.png").attr("alt","Space").attr("title","Space");
  }
  else if (loc["allowed"].indexOf('noaction') >= 0) {
    $("#st").attr("src","img/ActionW.png").attr("alt","Space").attr("title","Space");
  }
  else
  {
    if (loc["allowed"].indexOf('w') >= 0) {
      $("#st").attr("src","img/Straight.png").attr("alt","W").attr("title","W");
    }
    else {
      $("#st").attr("src","img/StraightW.png");
    }
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

// Carry out a user action (only called if allowed)
var doAction = function() {
  navok = false;
  $.getJSON("doaction?t=" + loc["tile"] + loc["face"], function(data) {
    loc = data
    $("#view").fadeTo(250, 0.7, function() {
      $("#view").attr("src","img/" + loc["zone"] + "/" + loc["image"]).fadeTo(250, 1);
      populateArrows();
      navok = true;
    });
  });
};
