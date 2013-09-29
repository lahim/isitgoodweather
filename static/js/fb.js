window.fbAsyncInit = function () {
    FB.init({
        appId: '307234952751343',
        channelUrl: '//isitgoodweather.com/channel.html',
        status: true,
        xfbml: true
    });
};

(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=307234952751343";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));