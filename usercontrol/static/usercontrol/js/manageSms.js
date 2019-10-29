var inputSwitch = $('#checkButton');
var btnSwitch = document.getElementById('switchButton');

btnSwitch.addEventListener('click', function() {
    // IMPORTANT !!!!!!!!!!!
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        url: '/manage_sms/',
        type: 'POST',
        dataType: 'json',
        data: {'active': inputSwitch[0].checked},
        success: function(data) {
            // display success message
        },
        error: function(error) {
            console.warn(error);
        },
    });
});