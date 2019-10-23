var btnEditUserInfos = document.getElementById('changeInfosUser');
var btnCancel = document.getElementById('cancel');
var btnConfirm = document.getElementById('confirmInfosUser');

btnEditUserInfos.addEventListener('click', function () {
    $('#contentUserInfos').hide(500, function () {
        $('#contentFormUserInfos').show(500);
    });

    $('#changeInfosUser').hide(500, function () {
        $('#cancel').show(500);
        $('#confirmInfosUser').show(500);
    });
});

btnCancel.addEventListener('click', function () {
    $('#contentFormUserInfos').hide(500, function () {
        $('#contentUserInfos').show(500);
    });

    $('#cancel').hide(500, function () {
        $('#changeInfosUser').show(500);
    });
    $('#confirmInfosUser').hide(500);
});

btnConfirm.addEventListener('click', function () {
    var lastName = document.getElementById('id_last_name');
    var firstName = document.getElementById('id_first_name');
    var pseudo = document.getElementById('id_pseudo');
    var email = document.getElementById('id_email');
    var phoneNumber = document.getElementById('id_phone_number');
    var csrftoken = getCookie('csrftoken');
    var infosUserChanged = [
        lastName.value,
        firstName.value,
        pseudo.value,
        email.value,
        phoneNumber.value
    ];

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        url: '/edit_infos/',
        type: 'POST',
        dataType: 'json',
        data: {
            'last_name': infosUserChanged[0],
            'first_name': infosUserChanged[1],
            'pseudo': infosUserChanged[2],
            'email': infosUserChanged[3],
            'phone': infosUserChanged[4],
        },
        success: function(data) {
            if (data['success']) {
                var listInfos = [
                    document.getElementById('userLastName'),
                    document.getElementById('userFirstName'),
                    document.getElementById('userPseudo'),
                    document.getElementById('userEmail'),
                    document.getElementById('userPhone')
                ];
                for (let i = 0; i < listInfos.length; i++) {
                    if (infosUserChanged[i] !== ""){
                        listInfos[i].innerText = infosUserChanged[i];   
                    } else {
                        // pass
                    }
                }
                $('#contentFormUserInfos').hide(500, function () {
                    $('#contentUserInfos').show(500);
                });

                $('#cancel').hide(500, function () {
                    $('#changeInfosUser').show(500);
                });
                $('#confirmInfosUser').hide(500);

            } else {
                var errorMessage = document.getElementById('messageError');
                errorMessage.classList.remove('d-none');
            }
        },
        error: function (error) {
            console.warn(error);
        },
    });
});