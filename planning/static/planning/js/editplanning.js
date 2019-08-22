function editPlanning(user, btn) {
    $('#trDish'+user).remove();
    btn.setAttribute('disabled', '');

    $('#modalBoxEdit').modal();

    var btnValideEdit = document.getElementById('confirmEdit');
    btnValideEdit.addEventListener('click', function () {
        var choiceMonday = document.getElementById(`selectLundiUser${user}`);
        var choiceTuesday = document.getElementById(`selectMardiUser${user}`);
        var choiceWednesday = document.getElementById(`selectMercrediUser${user}`);
        var choiceThursday = document.getElementById(`selectJeudiUser${user}`);
        var choiceFriday = document.getElementById(`selectVendrediUser${user}`);
        var choiceSaturday = document.getElementById(`selectSamediUser${user}`);
        var choiceSunday = document.getElementById(`selectDimancheUser${user}`);
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
                'monday': choiceMonday.value,
                'tuesday': choiceTuesday.value,
                'wednesday': choiceWednesday.value,
                'thursday': choiceThursday.value,
                'friday': choiceFriday.value,
                'saturday': choiceSaturday.value,
                'sunday': choiceSunday.value
            },
            success: function (data) {
                if (data['ResponseServeur']) {
                    var trDish = $('#trDish'+user).children();
                    for (let i = 0; i < trDish.length; i++) {
                        if (i < 7) {
                            document.getElementById(`dish-day${i+1}-user${user}`).textContent = listChoice[i]
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