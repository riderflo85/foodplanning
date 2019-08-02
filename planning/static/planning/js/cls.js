class Planning {
    id_user = NaN;
    week = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche', '#'];

    set_user_planning(){
        var User = $('#listAllUser')[0].value;
        var dictUser = JSON.parse(User);
        var nameUser = dictUser.name;
        this.id_user = Number(dictUser.pk);
        return nameUser;
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

        for (let i = 0; i < this.week.length; i++) {
            var baliseTd = `<td id='td${this.id_user}${i}'></td>`;
            $(baliseTd).appendTo(tr_body);

            var td = document.getElementById(`td${this.id_user}${i}`);
            if (this.week[i] === "#") {
                var baliseDivBtn = `<div class='d-flex-inline' id='divBtn${this.id_user}'></div>`;
                $(baliseDivBtn).appendTo(td);

                var divBtn = document.getElementById(`divBtn${this.id_user}`);
                var btnCheck = `<button type='button' class='btn btn-success' id='btnValidPlanning${this.id_user}'><i class='fas fa-check'></i></button>`;
                var btnEdit = `<button type='button' class='btn btn-primary' id='btnEditPlanning${this.id_user}'><i class='fas fa-pencil-alt'></i></button>`;
                var btnRemove = `<button type='button' class='btn btn-danger' id='btnRemovePlanning${this.id_user}'><i class='fas fa-trash-alt'></i></button>`;
                $(btnCheck).appendTo(divBtn);
                $(btnEdit).appendTo(divBtn);
                $(btnRemove).appendTo(divBtn);
            }else {
                var baliseSelect = `<select name='${this.week[i]}' class='custom-select' id='${this.week[i]}-pl-${this.id_user}'></select>`;
                var baliseOptionDefault = `<option selected>Choisissez un plat</option>`;
                $(baliseSelect).appendTo(td);

                var select = document.getElementById(`${this.week[i]}-pl-${this.id_user}`);
                $(baliseOptionDefault).appendTo(select);
            }
            
        }

        return table;
    }
}
