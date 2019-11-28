try {
    var btnSeeAnotherPlanningAm = document.getElementById('btnSeeOtherPlanningAm');

    btnSeeAnotherPlanningAm.addEventListener('click', function() {
        $('#modalBoxAnotherPlanningAm').modal()
    });    
} catch (error) {
    var btnSeeAnotherPlanningPm = document.getElementById('btnSeeOtherPlanningPm');

    btnSeeAnotherPlanningPm.addEventListener('click', function () {
        $('#modalBoxAnotherPlanningPm').modal()
    });
}