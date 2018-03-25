$(function(){
    //you can now use $ as your jQuery object.
    $('.message a').click(function(){
        $('div.form-page').animate({height: "toggle", opacity: "toggle"}, "slow");
    });

    $('button[id=create]').click(function(){
        var user = $('div.register-form input[id=register-user]').val();
        var password = $('div.register-form input[id=register-password]').val();
        $.ajax({
            url: '/user/register',
            data: {'user': user, 'password': password},
            type: 'POST',
            success: function(response) {
                window.location.response;
            },
            error: function(error) {
                error_handler(error);
            }
        });
    });

    $('button[id=login]').click(function(){
        var user = $('div.login-form input[id=login-user]').val();
        var password = $('div.login-form input[id=login-password]').val();
        $.ajax({
            url: '/user/login',
            data: {'user': user, 'password': password},
            type: 'POST',
            success: function(response) {
                window.location = response;
            },
            error: function(error) {
                error_handler(error);
            }
        });
    });
});


