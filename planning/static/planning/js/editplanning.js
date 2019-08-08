function editPlanning(user, btn) {
    var allSelect = document.getElementsByClassName('listing-for-disabled-' + user);
    $('#trDish'+user).remove();
    btn.setAttribute('disabled', '');

    for (let i = 0; i < allSelect.length; i++) {
        allSelect[i].removeAttribute('disabled');
    }
}