$(function(){
    $(document).keypress(function(e){
        var new_thread = $('input[id=new_thread]').val();
        if (new_thread != '') {
            if (e.which == 13){
                $.ajax({
                    url: '/threads/' + new_thread,
                    type: 'GET',
                    success: function(response) {
                        window.location = "/list_threads";
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
            }
        }
    });
});