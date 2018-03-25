$(function(){
    Notification.requestPermission();

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
                error_handler(error);
            }
        });
    });

    $(document).keypress(function(e){
        if (e.which == 13){
            $("button").click();
        }
    });


    var count_thread = function(count) {
        var thread_id = $('div[id=thread_id]').html();
        $.ajax({
            url: '/threads/' + thread_id + '/count_messages',
            type: 'GET',
            success: function(response) {
                delta = parseInt(response) - parseInt(count);
                if (delta > 0) {
                    notify(delta);
                }
                count_thread(response);
            },
            error: function(error) {
                error_handler(error);
            }
        });
    }

    var notify = function(messages_count) {
        // Let's check whether notification permissions have already been granted
        if (Notification.permission === "granted") {
            // If it's okay let's create a notification
            var notification = messages_count == '1' ? messages_count + " unread message" : messages_count + " unread messages";
            var notification = new Notification(notification);
        }
    }
});