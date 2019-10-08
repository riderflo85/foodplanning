function eventButton(id_user) {
    var btnCheck = document.getElementById('btnValidPlanning' + id_user);
    var btnEdit = document.getElementById('btnEditPlanning' + id_user);
    var btnRemove = document.getElementById('btnRemovePlanning' + id_user);
    var amOrPm = document.getElementById('momentDay').innerText;

    btnCheck.addEventListener('click', function () {
        validatePlanning(id_user, btnCheck, amOrPm);
        btnEdit.removeAttribute('disabled');
    });

    btnEdit.addEventListener('click', function () {
        editPlanning(id_user, btnEdit, amOrPm);
        // btnCheck.removeAttribute('disabled');
    });

    btnRemove.addEventListener('click', function () {
        removePlanning(id_user, amOrPm);
    });
}

function addNotifWithButton(id_user) {
    var btnAddNotif = document.getElementById('btnNotif' + id_user);

    btnAddNotif.addEventListener('click', function () {
        addNotification(id_user);
    });
}