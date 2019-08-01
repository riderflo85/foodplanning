function addPlanning() {
    var btnAddPlanning = document.getElementById('btnAddPlanning');
    var btnSave = document.getElementById('saveUserNewPlanning');
    var divContent = $('#divContent');


    btnAddPlanning.addEventListener('click', function () {
        $('#modalBoxAddNewPlanning').modal();
    });

    btnSave.addEventListener('click', function () {
        let test = new Planning();
        let username = test.get_user();
        console.log(test.get_user());

        var baliseTitlePlannig = "<p class='lead text-white mt-5'>Planning pour "+username+"</p>";
        $(baliseTitlePlannig).appendTo(divContent);
    });
}

