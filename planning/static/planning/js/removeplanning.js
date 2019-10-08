function removePlanning(user, amOrPm) {
    $('#modalBoxRemoveNewPlanning').modal();
    var btnValideRemoved = document.getElementById('confirmUserRemovePlanning');

    btnValideRemoved.addEventListener('click', function () {
        let user_planning = document.getElementById('userPlanning'+user);
        let table = document.getElementById('table'+user);
        var idPlanning = document.getElementById('idUserPlanning').textContent;

        var csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: '/planning/remove',
            type: 'POST',
            dataType: 'json',
            data: {'id_planning': idPlanning, 'momentDay': amOrPm},
            success: function (data) {
                if (data['ServeurResponse']) {
                    user_planning.classList.remove('rollIn');
                    table.classList.remove('rollIn');
                    user_planning.classList.add('rollOut');
                    table.classList.add('rollOut');
                    table.addEventListener('animationend', function () {
                        $('#userPlanning' + user).remove();
                        $('#table' + user).remove();
                        $('#idUserPlanning' + user).remove();
                    });
                }
            },
            error: function (error) {
                console.log(error);
            },
        });
    });
}