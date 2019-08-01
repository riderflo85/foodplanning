function addPlanning() {
    var btnAddPlanning = document.getElementById('btnAddPlanning');

    btnAddPlanning.addEventListener('click', function () {
        $('#modalBoxAddNewPlanning').modal();
    });
}