"use strict";

let luvut = [];

for(let i = 0; i < 5; i++) {
    let luku = Number(prompt("Syötä luku: "));
    luvut.push(luku);
}


for (let i = 4; i >= 0; i--) {
    console.log(luvut[i]);
}