
$(document).ready(function () {
    setStyle();
    getLocationWithWeather();
});

$(window).resize(function () {
    setStyle();
});

function setStyle() {
    var height = $(document).height();
    var paddingTop = (height / 2) - 50;

    $('#message').css('padding-top', paddingTop);
}

function getLocationWithWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(get_weather_message);
    }
    else {
        $('#message').html("Geolocation is not supported by this browser.");
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

            $('#message').find('h1').html(weather_message);
            if (css_class) {
                $('#message').addClass(css_class);
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