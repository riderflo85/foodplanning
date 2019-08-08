function addPlanning() {
    var btnAddPlanning = document.getElementById('btnAddPlanning');
    var btnSaveNew = document.getElementById('saveUserNewPlanning');
    var btnSaveRemove = document.getElementById('saveUserRemovePlanning');
    var divContent = $('#divContent');


    btnAddPlanning.addEventListener('click', function () {
        $('#modalBoxAddNewPlanning').modal();
    });

    btnSaveNew.addEventListener('click', function () {
        let planningFood = new Planning();
        let username = planningFood.set_user_planning();

        var baliseTitlePlannig = `<p class='lead text-white mt-5 animated rollIn' id='userPlanning${planningFood.id_user}'>Planning pour ${username}</p>`;
        $(baliseTitlePlannig).appendTo(divContent);
        
        planningFood.new_planning(divContent);
    });
    

}

