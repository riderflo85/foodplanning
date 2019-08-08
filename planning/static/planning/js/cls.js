class Planning {
    id_user = null;
    week = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche', '#'];

    set_user_planning(){
        var User = $('#listAllUser')[0].value;
        var dictUser = JSON.parse(User);
        var nameUser = dictUser.name;
        this.id_user = Number(dictUser.pk);
        return nameUser;
    }

    get_all_dish() {
        var csrftoken = getCookie('csrftoken');

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        return new Promise((resolve, reject) => {

            $.ajax({
                url: '/liste_des_plats/all_dish',
                type: 'GET',
                success: function (data) {
                    resolve(data);
                },
                error: function (error) {
                    reject(error);
                    console.log(error);
                },
            });
        });
    }

    new_planning(content) {
        var baliseTable = `<table class='table table-striped table-dark' id='table${this.id_user}'></table>`;
        var headTable = `<thead id='thead${this.id_user}'></thead>`;
        var bodyTable = `<tbody id='tBody${this.id_user}'></tbody>`;
        var trHead = `<tr id='trHead${this.id_user}'></tr>`;
        var thHead = `<th scope='col' id='thHead${this.id_user}'>`;
        var trBody = `<tr id='trBody${this.id_user}'></tr>`;
        
        $(baliseTable).appendTo(content);

        var table = document.getElementById(`table${this.id_user}`);
        $(headTable).appendTo(table);

        var thead = document.getElementById(`thead${this.id_user}`);
        $(trHead).appendTo(thead);

        var tr = document.getElementById(`trHead${this.id_user}`);
        for (let i = 0; i < this.week.length; i++) {
            var balise = thHead + this.week[i] + '</th>';
            $(balise).appendTo(tr);
        }

        $(bodyTable).appendTo(table);
        var tbody = document.getElementById(`tBody${ this.id_user }`);

        $(trBody).appendTo(tbody);
        var tr_body = document.getElementById(`trBody${this.id_user}`);

        // Promise()
        const onSucces = data => {
            for (let i = 0; i < this.week.length; i++) {
                var baliseTd = `<td id='td${this.id_user}${i}'></td>`;
                $(baliseTd).appendTo(tr_body);

                var td = document.getElementById(`td${this.id_user}${i}`);
                if (this.week[i] === "#") {
                    var baliseDivBtn = `<div class='d-flex-inline' id='divBtn${this.id_user}'></div>`;
                    $(baliseDivBtn).appendTo(td);

                    var divBtn = document.getElementById(`divBtn${this.id_user}`);
                    var baliseBtnCheck = `<button type='button' class='btn btn-success' id='btnValidPlanning${this.id_user}'><i class='fas fa-check'></i></button>`;
                    var baliseBtnEdit = `<button type='button' class='btn btn-primary' id='btnEditPlanning${this.id_user}' disabled><i class='fas fa-pencil-alt'></i></button>`;
                    var baliseBtnRemove = `<button type='button' class='btn btn-danger' id='btnRemovePlanning${this.id_user}'><i class='fas fa-trash-alt'></i></button>`;
                    $(baliseBtnCheck).appendTo(divBtn);
                    $(baliseBtnEdit).appendTo(divBtn);
                    $(baliseBtnRemove).appendTo(divBtn);

                    /* ****** Gestionnaire d'événement pour les trois boutons des plannings ******  */
                    var btnCheck = document.getElementById('btnValidPlanning' + this.id_user);
                    var btnEdit = document.getElementById('btnEditPlanning' + this.id_user);
                    var btnRemove = document.getElementById('btnRemovePlanning' + this.id_user);
                    var user_id = this.id_user;

                    btnCheck.addEventListener('click', function () {
                        validatePlanning(user_id, btnCheck);
                        btnEdit.removeAttribute('disabled');
                    });

                    btnEdit.addEventListener('click', function () {
                        editPlanning(user_id, btnEdit);
                        btnCheck.removeAttribute('disabled');
                    });

                    btnRemove.addEventListener('click', function () {
                        removePlanning(user_id);
                    });
                    /* ***************************************************************************  */


                } else {
                    var baliseSelect = `<select name='${this.week[i]}' class='custom-select listing-for-disabled-${this.id_user}' id='${this.week[i]}-pl-${this.id_user}'></select>`;
                    var baliseOptionDefault = `<option selected>Choisissez un plat</option>`;
                    $(baliseSelect).appendTo(td);

                    var select = document.getElementById(`${this.week[i]}-pl-${this.id_user}`);
                    $(baliseOptionDefault).appendTo(select);

                    for (let i = 0; i < data.Data.length; i++) {
                        var baliseDish = `<option value='${data.Data[i]}'>${data.Data[i]}</option>`;
                        $(baliseDish).appendTo(select);
                    }
                }
            }
        }

        const onFailure = error => {
            console.log(error);
        }

        const myRequest = this.get_all_dish();
        myRequest.then(onSucces).catch(onFailure);

        return table;
    }
}
