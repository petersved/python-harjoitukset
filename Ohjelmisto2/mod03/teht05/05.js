"use strict";

let luvut = [];

while (true) {
    let luku = Number(prompt("Anna luku:"));

    if (luvut.includes(luku)) {
        console.log("Luku on jo annettu!");
        break;
    }

    luvut.push(luku);
}

luvut.sort((a, b) => a - b);

for (let i = 0; i < luvut.length; i++) {
    console.log(luvut[i]);
}