"use strict";

let osallistujat = [];

let määrä = Number(prompt("Kuinka monta osallistujaa on?"));


for (let i = 0; i < määrä; i++) {
    let nimi = prompt("Anna osallistujan nimi:");
    osallistujat.push(nimi);
}

osallistujat.sort();

let lista = document.getElementById("target");

for (let i = 0; i < osallistujat.length; i++) {
    document.getElementById("target").innerHTML +=
        "<li>" + osallistujat[i] + "</li>"
}