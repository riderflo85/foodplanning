function removeMessageNotPlanning() {
    try {
        var forContent = document.getElementById('divContent');
        var messageNotPlanning = document.getElementById('messageNotPlanning');
        messageNotPlanning.remove();
        forContent.classList.remove('text-center');
        forContent.classList.add('col-lg-10', 'offset-lg-1');
        return true;

    } catch (error) {
        return error;
    }
}


function addPlanning() {
    var btnAddPlanning = document.getElementById('btnAddPlanning');
    // var btnSaveNew = document.getElementById('saveUserNewPlanning');
    var divContent = $('#divContent');
    
    
    // btnAddPlanning.addEventListener('click', function () {
    //     $('#modalBoxAddNewPlanning').modal();
    // });
    
    btnAddPlanning.addEventListener('click', function () {
        var check = removeMessageNotPlanning();
        if (check) {
            let planningFood = new Planning();
            let username = planningFood.set_user_planning();
    
            var baliseTitlePlanning = `<p class='lead text-white mt-5 animated fadeIn' id='userPlanning${planningFood.id_user}'>Planning pour ${username}</p>`;
            var baliseIdPlanningUser = `<p class="d-none animated fadeIn" id="idUserPlanning">${planningFood.id_user}</p>`;
            $(baliseTitlePlanning).appendTo(divContent);
            $(baliseIdPlanningUser).appendTo(divContent);
            
            planningFood.new_planning(divContent);
            btnAddPlanning.setAttribute('disabled', 'true');
        } else {
            console.warning(check);
        }
    });
}

