function deleteDish() {
    var btnDeleteDish = document.getElementById('btnDeleteDish');

    btnDeleteDish.addEventListener('click', function () {
        $('#modalBoxDeleteDish').modal();
    });
}