window.onload = function () {
    addPlanning();
    if (document.getElementById('varCheck').textContent === 'true') {
        var user_id = document.getElementById('idUserDb').innerHTML;
        eventButton(user_id);
        addNotifWithButton(user_id);
    } else {
        // pass
    }
}