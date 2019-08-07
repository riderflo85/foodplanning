function removePlanning(user) {
    $('#modalBoxRemoveNewPlanning').modal();
    var btnValideRemoved = document.getElementById('confirmUserRemovePlanning');

    btnValideRemoved.addEventListener('click', function () {
        $('#userPlanning'+user).remove();
        $('#table'+user).remove();
    });
}