var btnEditPwd = document.getElementById('changePwd');
var btnConfirmPwd = document.getElementById('confirmPwd');
var btnCancelPwd = document.getElementById('cancelPwd');
var inputForm = document.getElementById('password');
var inputConfirmForm = document.getElementById('confirmPassword');
var newPasswd = '';

btnEditPwd.addEventListener('click', function() {
    $('#partPasswd').show(500);
    $('#contentFormPwd').show(500);
    $('#changePwd').hide(500, function() {
        $('#cancelPwd').show(500);
        $('#confirmPwd').show(500);
    });
});

btnCancelPwd.addEventListener('click', function() {
    $('#partPasswd').hide(500);
    $('#cancelPwd').hide(500);
    $('#confirmPwd').hide(500);
    $('#contentFormPwd').hide(500, function() {
        $('#changePwd').show(500);
    });
});

inputForm.addEventListener('blur', function() {
    if (this.value.length < 8){
        this.classList.add('is-invalid');
        document.getElementById('notMatchRegPwd').classList.remove('d-none');
    }else{
        if (this.classList.contains('is-invalid')){
            this.classList.remove('is-invalid');
            this.classList.add('is-valid');
            document.getElementById('notMatchRegPwd').classList.add('d-none');
        }else{
            this.classList.add('is-valid');
        }
    }
});

inputConfirmForm.addEventListener('keyup', function() {
    if (inputForm.value === this.value){
        this.classList.remove('is-invalid');
        this.classList.add('is-valid');
        newPasswd = this.value;
    }else{
        if (this.classList.contains('is-invalid')){
            //pass
        }else{
            this.classList.add('is-invalid');
        }
    }
});

btnConfirmPwd.addEventListener('click', function() {

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        url:'/change_pwd/',
        type: 'POST',
        dataType: 'json',
        data: {'new_pwd': newPasswd},
        success: function(data) {
            if (data['success']) {
                $('#partPasswd').hide(500);
                $('#cancelPwd').hide(500);
                $('#confirmPwd').hide(500);
                $('#contentFormPwd').hide(500, function () {
                    $('#changePwd').show(500);
                });
            }else{
                // pass
            }
        },
        error: function(error) {
            console.warn(error);
        },
    });
});