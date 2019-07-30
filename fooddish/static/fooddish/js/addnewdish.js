function addNewDish() {
    var btnAdd = document.getElementById('addNewDish');

    btnAdd.addEventListener('click', function () {
        $('#modalBoxAddDish').modal();
        console.log('test');
    });
}