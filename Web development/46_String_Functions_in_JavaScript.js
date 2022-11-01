var str = "This is a string";
console.log(str);

// First occurence of a substring
var position = str.indexOf('is');
console.log(position)

// Last occurence of a substring
position = str.lastIndexOf('is');
console.log(position)

// Substring from a string
// var substr = str.slice(1,7);
// var substr = str.substring(1,7);
var substr1 = str.substr(1, 3);
console.log(substr1)

var replaced = str.replace('string', 'Harry');
console.log(str)
console.log(replaced)
console.log(str.toUpperCase());
console.log(str.toLowerCase());
var newString = str.concat('New String')
console.log(newString)
var strWithWhitespaces = "   this contains        whitespaces   ";
console.log(strWithWhitespaces)
console.log(strWithWhitespaces.trim())
var char2 = str.charAt(2);
var char2 = str.charCodeAt(2); // Not very important
console.log(char2)

console.log(str[3])
