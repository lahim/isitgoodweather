
var opts = {
  lines: 16, // The number of lines to draw
  length: 0, // The length of each line
  width: 4, // The line thickness
  radius: 15, // The radius of the inner circle
  corners: 1, // Corner roundness (0..1)
  rotate: 0, // The rotation offset
  direction: 1, // 1: clockwise, -1: counterclockwise
  color: '#000', // #rgb or #rrggbb or array of colors
  speed: 0.9, // Rounds per second
  trail: 60, // Afterglow percentage
  shadow: false, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: 'auto', // Top position relative to parent in px
  left: 'auto' // Left position relative to parent in px
};

var target;
var spinner;

$(document).ready(function () {
    setStyle();
    target = document.getElementById('weather_message');
    spinner = new Spinner(opts).spin(target);
    getLocationWithWeather();
});

$(window).resize(function () {
    setStyle();
});

function setStyle() {
    var height = $(document).height();
    var paddingTop = (height / 2) - 50;

    $('div.message').css('padding-top', paddingTop);
//    $("#message").find("div[class=spinner]").css('top', height);
}

function getLocationWithWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(get_weather_message);
    }
    else {
        $('div.message').html("<h2>Geolocation is not supported by this browser.</h2>");
    }
}

function get_weather_message(position) {
    var uri = "/weather/" + position.coords.latitude + "," + position.coords.longitude;
    $.get(uri, {
        format: "json"
    })
        .done(function (data) {
            var attempt_number = data.attempt_number;
            var weather_message = data.weather_message;
            var weather = data.weather;
            var code = data.weather_code;
            var css_class = data.css_class;

            $("#weather_message").find("div[class=spinner]").hide();

            $('#weather_message').html(weather_message);
            if (css_class) {
                $('div.message').addClass(css_class);
            }
            saveCookie(attempt_number, weather, code);
        }
    );
}

function saveCookie(attemptNumber, weather, code) {
    var expires = new Date();
    var time = expires.getTime();
    time += 300 * 1000;
    expires.setTime(time)
    $.cookie('attempts_cookie', [attemptNumber, weather, code], { expires: expires, path: '/' });
}