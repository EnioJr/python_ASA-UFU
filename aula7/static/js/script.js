$(function() {
    $('#btn_register').click(function() {
        $.ajax({
            url: '/signUpUser',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#btn_message').click(function() {
        $.ajax({
            url: '/showMessage',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                if(response.redirect){
                    window.location.href = response.redirect
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });    
});