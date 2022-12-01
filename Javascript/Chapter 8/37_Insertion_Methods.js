let b = document.getElementsByTagName("div")[1];
b.innerHTML = b.innerHTML + '<h1>comment added through innerHTML</h1>';


let a = document.createElement("div");
a.innerHTML = '<h1>comment added through append method</h1>';
b.append(a);

let c = document.createElement("div");
c.innerHTML = '<h1>comment added through prepend method</h1>';
b.prepend(c);

let d = document.createElement("div");
d.innerHTML = '<h1>comment added through before method</h1>';
b.before(d);

let e = document.createElement("div");
e.innerHTML = '<h1>comment added through after method</h1>';
b.after(e);

// b.replaceWith("replaced")