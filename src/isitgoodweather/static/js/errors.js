
$(document).ready(function () {
    setStyle();
});

$(window).resize(function () {
    setStyle();
});

function setStyle() {
    var height = $(document).height();
    var paddingTop = (height / 2) - 50;

    $('#message').css('padding-top', paddingTop);
}