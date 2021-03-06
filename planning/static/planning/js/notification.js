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
    if ($('#checkUseSms')[0].textContent == 'False'){
        $('#modalBoxNotActived').modal();
    }else{
        $('#modalBoxNotification').modal();
        var btnNotif = document.getElementById('confirmNotification');
    
        btnNotif.addEventListener('click', function () {
            var days = document.getElementById('selectDay').value;
            var date = document.getElementById('dateNotif').value;
            var hours = document.getElementById('timeNotif').value;
            var message = document.getElementById('messageNotif').value;
    
            const OnSucces = data => {
                if (data['Response'] === true) {
                    console.log('La notification a bien été ajouter au gestionnaire de tache');
                    var dayForBadge = document.getElementById(`dish-day${days}-user${user}`);
                    var baliseBadge = ` <i class='badge badge-pill badge-warning'>notif</i>`;
                    $(baliseBadge).appendTo(dayForBadge);
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
}