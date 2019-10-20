var itemsNavMenu = [
    document.getElementById('nav-am'),
    document.getElementById('nav-pm'),
    document.getElementById('nav-dishs'),
    document.getElementById('nav-account'),
];

for (const i of itemsNavMenu) {
    for (const e of i.classList) {
        if (e === 'this-page') {
            i.classList.remove('this-page');
        }
    }
}

itemsNavMenu[2].classList.add('this-page');