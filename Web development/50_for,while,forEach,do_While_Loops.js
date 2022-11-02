console.log("This is tutorial 55");
let i = 0;
for (i = 0; i < 3; i++) {
    console.log(i);
}

let friends = ["Rohan", "Sanjeev", "Deepti", "Pooja", "SkillF"];
for (let index = 0; index < friends.length; index++) {
    console.log("Hello friend, " + friends[index]);
}

friends.forEach(function f(element) {
    console.log("Hello Friend, " + element + " to modern JavaScript");
});

for (element of friends) {
    console.log("Hello Friend, " + element + " to modern JavaScript again");
}

let employee = {
    name: "Harry",
    salary: 2,
    channel: "CWH"
}

// Use this loop to iterate over objects in JavaScript
for (key in employee) {
    console.log(`The ${key} of employee is ${employee[key]}`);
}

// while loop in js
let k = 0;
while (k < 4) {
    console.log(`${i} is less than 4`);
    k++;
}

// do while loop in js
let j = 34;
do {
    console.log(`${j} is less than 4 and we are inside do while loop`);
    j++;
} while (j < 4);

