"use strict";

const luku1 = Number(prompt("Anna ensimmäinen kokonaisluku:"));
const luku2 = Number(prompt("Anna toinen kokonaisluku:"));
const luku3 = Number(prompt("Anna kolmas kokonaisluku:"));

const summa = luku1 + luku2 + luku3
const keskiarvo = summa / 3
const tulo = luku1 * luku2 * luku3

document.querySelector("#target").innerHTML =
    "Summa: " + summa + "<br>" +
    "Tulo: " + tulo + "<br>" +
    "Keskiarvo: " + keskiarvo;