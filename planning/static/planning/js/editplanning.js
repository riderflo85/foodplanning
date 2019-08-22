function editPlanning(user, btn) {
    // $('#trDish'+user).remove();
    btn.setAttribute('disabled', '');

    $('#modalBoxEdit').modal();

    var btnValideEdit = document.getElementById('confirmEdit');
    btnValideEdit.addEventListener('click', function () {
        var choiceMonday = $(`#selectLundiUser${user} option:selected`);
        var choiceTuesday = $(`#selectMardiUser${user} option:selected`);
        var choiceWednesday = $(`#selectMercrediUser${user} option:selected`);
        var choiceThursday = $(`#selectJeudiUser${user} option:selected`);
        var choiceFriday = $(`#selectVendrediUser${user} option:selected`);
        var choiceSaturday = $(`#selectSamediUser${user} option:selected`);
        var choiceSunday = $(`#selectDimancheUser${user} option:selected`);
        var idPlanning = document.getElementById(`idUserPlanning${user}`);
        var csrftoken = getCookie('csrftoken');
        var listChoice = [choiceMonday, choiceTuesday, choiceWednesday, choiceThursday, choiceFriday, choiceSaturday, choiceSunday]

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: '/planning/update',
            type: 'POST',
            dataType: 'json',
            data: {
                'id': idPlanning.textContent,
                'monday': choiceMonday.val(),
                'tuesday': choiceTuesday.val(),
                'wednesday': choiceWednesday.val(),
                'thursday': choiceThursday.val(),
                'friday': choiceFriday.val(),
                'saturday': choiceSaturday.val(),
                'sunday': choiceSunday.val()
            },
            success: function (data) {
                if (data['ServeurResponse']) {
                    var trDish = $('#trDish'+user).children();
                    for (let i = 0; i < trDish.length; i++) {
                        if (i < 7) {
                            var foo = document.getElementById(`dish-day${i}-user${user}`);
                            foo.textContent = listChoice[i].text();
                        }else {
                            // pass
                        }

                    }
                }
            },
            error: function (error) {
                console.log(error);
            },
        });


    });
}