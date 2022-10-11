// Array---practice set
//question 1
let arr=[1,2,3,4,5,6]
let num=prompt("enter a number")
num=Number.parseInt(num)
let num2=arr.unshift(num)
console.log(arr)

//question 2
let a;
do {
    num2=prompt("enter a number")
    num2=Number.parseInt(num2)
    arr.push(num2)
} while (a!=0);
console.log(arr)

// question 3
let b=arr.filter((b2)=>{
    return b2%2==0;
})
console.log(b)

// question 4
let n = arr.map((x)=>{
  return x*x
})
console.log(n)

// question 5
let h=arr.reduce((h2,h3)=>{
    return h2*h3
})
console.log(h)