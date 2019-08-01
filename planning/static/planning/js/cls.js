class Planning {
    id_user = NaN;

    get_user(){
        var User = $('#listAllUser')[0].value;
        var dictUser = JSON.parse(User);
        var nameUser = dictUser.name;
        this.id_user = Number(dictUser.pk);
        return nameUser;
    }

    set_user_planning() {

    }

    new_planning() {

    }
}
