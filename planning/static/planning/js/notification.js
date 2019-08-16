function send_notification(date, time, msg) {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    return new Promise((resolve, reject) => {
        $.ajax({
            url: '/notif/set',
            type: 'POST',
            dataType: 'json',
            data: {
                'date': date,
                'time': time,
                'message': msg
            },
            success: function (data) {
                resolve(data);
            },
            error: function (error) {
                reject(error);
                console.log(error);
            },
        });
    });
}


function addNotification(user) {
    $('#modalBoxNotification').modal();
    var btnNotif = document.getElementById('confirmNotification');

    btnNotif.addEventListener('click', function () {
        var days = document.getElementById('selectDay').value;
        var date = document.getElementById('dateNotif').value;
        var hours = document.getElementById('timeNotif').value;
        var message = document.getElementById('messageNotif').value;

        const OnSucces = data => {
            if (data === true) {
                console.log('La notification a bien été ajouter au gestionnaire de tache');
            }else{
                console.warn("Une erreur est survenue, la notif n'a pas pu être ajoutée");
            }
        }

        const onFailure = error => {
            console.warn(error);
        }

        const newNotif = send_notification(date, hours, message);
        newNotif.then(OnSucces).catch(onFailure);

        console.log(days);
        console.log(date);
        console.log(hours);
        console.log(message);

    });
}