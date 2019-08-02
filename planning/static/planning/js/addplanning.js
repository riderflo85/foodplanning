function addPlanning() {
    var btnAddPlanning = document.getElementById('btnAddPlanning');
    var btnSave = document.getElementById('saveUserNewPlanning');
    var divContent = $('#divContent');


    btnAddPlanning.addEventListener('click', function () {
        $('#modalBoxAddNewPlanning').modal();
    });

    btnSave.addEventListener('click', function () {
        let planningFood = new Planning();
        let username = planningFood.set_user_planning();

        var baliseTitlePlannig = "<p class='lead text-white mt-5'>Planning pour "+username+"</p>";
        $(baliseTitlePlannig).appendTo(divContent);
        
        planningFood.new_planning(divContent);

    });
}

