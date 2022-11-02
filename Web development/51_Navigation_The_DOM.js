let main = document.getElementById('main');
console.log(main);
let nav = document.getElementById('nav');
console.log(nav);

let containers = document.getElementsByClassName('container');
console.log(containers);

//let sel = document.querySelector('#nav>li');
//console.log("Selector returns ", sel)

let sel = document.querySelectorAll('#nav>li');
console.log("Selector returns ", sel)

