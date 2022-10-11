// question no 1
// let age = prompt("Enter your age");
// age = Number.parseInt(age);
// const candrive = (age) => {
//     return age >= 18 ? true : false;
// }
// if (candrive(age)) {
//     alert("you can drive") 
// }
// else {
//     alert("you can't drive")
// }
// question no 2
// let age = prompt("Enter your age");
// age = Number.parseInt(age);
// runAgaim = true;
// while (runAgaim) {
//     const candrive = (age) => {
//         return age >= 18 ? true : false;
//     }
//     if (candrive(age)) {
//         alert("you can drive")
//     }
//     else {
//         alert("you can't drive")
//     }
//     runAgaim = confirm("do you want to enter your age again")
// }

// question 3
let age = prompt("Enter your age");
age = Number.parseInt(age);
runAgaim = true;
while (runAgaim) {
    const candrive = (age) => {
        return age >= 18 ? true : false;
    }
    if (candrive(age)) {
        alert("you can drive")
    }
    if (age < 0) {
        console.error("gadhe/gadhi sahi age daal")
    }
    else {
        alert("you can't drive")
    }
    runAgaim = confirm("do you want to enter your age again")
}

// question 4
let number = prompt("enter a number")
number = Number.parseInt(number)
if (number > 4) {
    location.href = "https://www.google.com"
}

// question 5
let color = prompt("enter a color")
document.body.style.background = color