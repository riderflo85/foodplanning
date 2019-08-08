function removePlanning(user) {
    $('#modalBoxRemoveNewPlanning').modal();
    var btnValideRemoved = document.getElementById('confirmUserRemovePlanning');

    btnValideRemoved.addEventListener('click', function () {
        let user_planning = document.getElementById('userPlanning'+user);
        let table = document.getElementById('table'+user);

        user_planning.classList.remove('rollIn');
        table.classList.remove('rollIn');
        user_planning.classList.add('rollOut');
        table.classList.add('rollOut');
        table.addEventListener('animationend', function () {
            $('#userPlanning'+user).remove();
            $('#table'+user).remove();
        });
    });
}