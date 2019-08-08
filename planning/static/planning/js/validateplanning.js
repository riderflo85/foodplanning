function validatePlanning(user, btn) {
    var allSelect = document.getElementsByClassName('listing-for-disabled-'+user);
    var trBody = $('#trBody'+user)
    var trBodyChildren = trBody.children();
    var tBody = $('#tBody'+user);
    var baliseTrBodyDish = `<tr id='trDish${user}' class='text-center'></tr>`;
    $(baliseTrBodyDish).appendTo(tBody);
    
    var trDish = $('#trDish'+user);

    for (let i = 0; i < trBodyChildren.length; i++) {
        if (i < 7) {
            var dish = trBodyChildren[i].childNodes[0].value;
            var baliseTd = `<td id='dish-day${i}-user${user}'>${dish}</td>`;
            $(baliseTd).appendTo(trDish);
        }else {
            var baliseBtnNotif = `<td><button type='button' class='btn btn-warning text-white' id='btnNotif${user}'><i class='fas fa-bell'></i></button></td>`;
            $(baliseBtnNotif).appendTo(trDish);
            var btnNotif = document.getElementById('btnNotif'+user);
            btnNotif.addEventListener('click', function () {
                addNotification(user);
            });
        }
    }
    btn.setAttribute('disabled', '');
    for (let i = 0; i < allSelect.length; i++) {
        allSelect[i].setAttribute('disabled', '');
    }
}