function validatePlanning(user, btn, amOrPm) {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var allSelect = document.getElementsByClassName('listing-for-disabled-'+user);
    var trBody = $('#trBody'+user)
    var trBodyChildren = trBody.children();
    var tBody = $('#tBody'+user);
    var baliseTrBodyDish = `<tr id='trDish${user}' class='text-center'></tr>`;
    $(baliseTrBodyDish).appendTo(tBody);
    
    var trDish = $('#trDish'+user);
    var dictDish = [];

    for (let i = 0; i < trBodyChildren.length; i++) {

        if (i < 7) {
            var dish = trBodyChildren[i].childNodes[0].value;
            dictDish.push(dish);
            var baliseTd = `<td id='dish-day${i}-user${user}'>${dish}</td>`;
            $(baliseTd).appendTo(trDish);
        }

        else {
            var baliseBtnNotif = `<td><button type='button' class='btn btn-warning text-white' id='btnNotif${user}'><i class='fas fa-bell'></i></button></td>`;
            $(baliseBtnNotif).appendTo(trDish);
            addNotifWithButton(user);
        }
    }
    btn.setAttribute('disabled', '');
    for (let i = 0; i < allSelect.length; i++) {
        allSelect[i].setAttribute('disabled', '');
    }

    $.ajax({
        url: '/planning/set',
        type: 'POST',
        dataType: 'json',
        data: {
            'days1':dictDish[0],
            'days2':dictDish[1],
            'days3':dictDish[2],
            'days4':dictDish[3],
            'days5':dictDish[4],
            'days6':dictDish[5],
            'days7':dictDish[6],
            'momentDay': amOrPm
        },
        success: function (data) {
            var baliseIdPlanning = `<p class='d-none' id='idUserPlanning${user}'>${data['id_planning']}</p>`;
            $(document.getElementById(`userPlanning${user}`)).after(baliseIdPlanning);
        },
        error: function (error) {
            console.log(error);
        },
    });
}