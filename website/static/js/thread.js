$(function(){
    $('button').click(function(){
        var body = $('input[id=body]').val();
        var thread = $('h2[id=subject').html();
        $.ajax({
            url: '/thread/post_content',
            data: {'thread': thread, 'body': body},
            type: 'POST',
            success: function(response) {
                obj = JSON.parse(response);
                console.log(obj)
                var first_char_in_name = obj.created_by.charAt(0);
                var chat = '<li class="left clearfix">'
                         +   '<span class="chat-img pull-left">'
                         +       '<img src="/static/icon/png/' + first_char_in_name + '.png" alt="User Avatar" class="img-circle" />'
                         +   '</span>'
                         +   '<div class="chat-body clearfix">'
                         +      '<div class="header">'
                         +         '<strong class="primary-font">' + obj.created_by + '</strong>'
                         +         '<small class="pull-right text-muted">'
                         +            '<span class="glyphicon glyphicon-time"></span>' + obj.created_date
                         +         '</small>'
                         +      '</div>'
                         +      '<p>' + obj.body + '</p>'
                         +    '</div>'
                         + '</li>'
                         + $('ul[class=chat]').html()
                $('ul[class=chat]').html(chat);
            },
            error: function(error) {
                if (error.status == 400) {
                    window.location = "error/400.html";
                } else {
                    console.log(error);
                    window.location = "error/unknown.html";
                }
            }
        });
    });

    $(document).keypress(function(e){
        if (e.which == 13){
            $("button").click();
        }
    });
});