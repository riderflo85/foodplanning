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
            if (dish === "Choisissez un plat"){
                var baliseTd = `<td id='dish-day${i}-user${user}'>???</td>`;
            } else {
                var baliseTd = `<td id='dish-day${i}-user${user}'>${dish}</td>`;
            }
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
            'momentDay': amOrPm,
            'monday':dictDish[0],
            'tuesday':dictDish[1],
            'wednesday':dictDish[2],
            'thursday':dictDish[3],
            'friday':dictDish[4],
            'saturday':dictDish[5],
            'sunday':dictDish[6],
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