function deleteDish() {
    var btnDeleteDish = document.getElementById('btnDeleteDish');
    var btnValideDelete = document.getElementById('btnConfirmDelete');

    btnDeleteDish.addEventListener('click', function () {
        $('#modalBoxDeleteDish').modal();
    });

    btnValideDelete.addEventListener('click', function () {
        var dishSeleted = document.getElementById('selectDeleteDish');
        var csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: '/liste_des_plats/delete_dish/',
            type: 'POST',
            dataType: 'json',
            data: {'id': dishSeleted.value},
            success: function (data) {
                if (data['removed'] === true){
                    $('#element' + dishSeleted.value).remove();
                    $('#' + dishSeleted.value).remove();
                } else {
                    // pass
                }
            },
            error: function (data) {
                console.warn(data);
            },
        });

    });
}