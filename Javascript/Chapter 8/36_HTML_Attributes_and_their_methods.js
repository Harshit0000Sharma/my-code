let first = document.getElementById("first");
let a = first.getAttribute("class");
let b = first.hasAttribute("f2");
console.log(a);
console.log(b);

let second = document.getElementById("second");
second.setAttribute("class", "f2");
second.setAttribute("hidden", "true");

let third = document.getElementById("third");
third.removeAttribute("class");

let fourth = document.getElementById("fourth")
console.log(fourth.dataset);
console.log(fourth.dataset.name);
console.log(fourth.dataset.sname);