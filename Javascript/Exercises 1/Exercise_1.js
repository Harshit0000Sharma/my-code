let x = Math.floor((Math.random() * 100) + 1);
x= Number.parseInt(x)
let chances=0
chances=Number.parseInt(chances)
chances_left=10
chances_left= Number.parseInt(chances_left)

let a;
while (a!=x) {

    let num= prompt("Enter your guess");
    num= Number.parseInt(num)
    chances +=1;
    chances_left-=1;
    if(chances_left == 0) {
        console.log("you lost the game")
        break;
    }
    else if (num>x) {
        console.log("think of  a smaller number")
        console.log("you have ",chances_left," chances left")
    }
    else if(num<x) {
        console.log("think of a larger number")
        console.log("you have ",chances_left," chances left") 
    }
    else if (num=x) {
        console.log("you guessed it right .It is ",num);
        console.log("It take you ",chances-1,"chances")
        break;
    }
}