// Chapter 2 - Q1
let age = prompt("What is your age?")
age = Number.parseInt(age)
if (age > 10 && age < 20) {
  console.log("Your age lies between 10 and 20")
}
else {
  console.log("Your age doesnt lies between 10 and 20")
}
 
// Chapter 2 - Q2
switch (age) {
  case '12':
    console.log("Your age is 12")
    break
  case '13':
    console.log("Your age is 13")
    break
  case '14':
    console.log("Your age is 14")
    break
  case '15':
    console.log("Your age is 15")
    break
  default:
    console.log("Your age is not special")
}

// Chapter 2 - Q3
let num = prompt("enter a number");
num = Number.parseInt(num)
if (num%2==0&&num%3==0){
    alert("number is divisible by 2 and 3")
}
else{
    alert("number is not divisible by 2 and 3")
}

// Chapter 2 - Q4
if (num%2==0 || num%3==0){
    alert("number is divisible either by 2 or 3")
}
else{
    alert("number is not divisible by 2 and 3")
}

// Chapter 2 - Q5
let a = age > 18 ? "You can drive" : "You cannot drive"
console.log(a)