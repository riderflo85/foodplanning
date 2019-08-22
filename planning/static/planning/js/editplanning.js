function editPlanning(user, btn) {
    $('#trDish'+user).remove();
    btn.setAttribute('disabled', '');

    $('#modalBoxEdit').modal();

    var btnValideEdit = document.getElementById('confirmEdit');
    btnValideEdit.addEventListener('click', function () {
        var choiceMonday = document.getElementById(`selectLundiUser${user}`).value;
        var choiceTuesday = document.getElementById(`selectMardiUser${user}`).value;
        var choiceWednesday = document.getElementById(`selectMercrediUser${user}`).value;
        var choiceThursday = document.getElementById(`selectJeudiUser${user}`).value;
        var choiceFriday = document.getElementById(`selectVendrediUser${user}`).value;
        var choiceSaturday = document.getElementById(`selectSamediUser${user}`).value;
        var choiceSunday = document.getElementById(`selectDimancheUser${user}`).value;

        console.log(choiceMonday);

    });
}