"use strict";

let koirat = []

for (let i = 0; i < 6; i++) {
    let nimi = prompt("Anna koiran nimi:");
    koirat.push(nimi);
}

koirat.sort();

for (let i = koirat.length - 1; i >= 0; i--) {
    document.getElementById("target").innerHTML +=
        "<li>" + koirat[i] + "</li>";
}