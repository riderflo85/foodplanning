function addNotification(user) {
    $('#modalBoxNotification').modal();
    var btnNotif = document.getElementById('confirmNotification');

    btnNotif.addEventListener('click', function () {
        var days = document.getElementById('selectDay').value;
        var date = document.getElementById('dateNotif').value;
        var hours = document.getElementById('timeNotif').value;
        var message = document.getElementById('messageNotif').value;

        console.log(days);
        console.log(date);
        console.log(hours);
        console.log(message);
    });
}