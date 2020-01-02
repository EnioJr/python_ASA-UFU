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
    $('#btn_load').click(function() {
        $.ajax({
            url: '/testJsonObject',
            callback: 'callback',
            crossDomain: true,
            contentType: 'application/json; charset=utf-8',
            dataType: 'application/json',
            complete: function(data){
                alert(data.status);//51000
                var myResult = data
                console.log(myResult);
                var myDict = JSON.parse(data.responseText);
                var len = myDict.length;
                var list_html = "<ol>";
                for(var i = 0; i < len; i++){
                    list_html += "<li>" + myDict[i].nome + " " + myDict[i].idade + " " + myDict[i].curso + "</li>";
                    console.log(myDict[i])
                }
                list_html += "</ol>"
                $("#jsonlist").html(list_html);
            },
            error: function(error){
                console.log(error);
            }
        });
    });    
});
