var itemsNavMenu = [
    document.getElementById('nav-am'),
    document.getElementById('nav-pm'),
    document.getElementById('nav-dishs')
];

for (const i of itemsNavMenu) {
    for (const e of i.classList){
        if (e === 'this-page'){
            i.classList.remove('this-page');
        }
    }
}

itemsNavMenu[1].classList.add('this-page');