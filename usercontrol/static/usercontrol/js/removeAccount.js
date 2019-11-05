var btnRemoveAccount = document.getElementById('deleteAccount');
var btnConfirmRemoveAccount = document.getElementById('confirmRemoveAccount');

btnRemoveAccount.addEventListener('click', function() {
    // Display modal box for user confirm remove account
    $('#modalRemoveAccount').modal();

    btnConfirmRemoveAccount.addEventListener('click', function() {
        var csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: '/remove_account/',
            type: 'POST',
            dataType: 'json',
            data: {'confirm': 'true'},
            error: function(error) {
                console.warn(error);
            },
        });
    });
});