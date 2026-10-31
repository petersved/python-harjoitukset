"use strict";

const nimi = prompt("Mikä sinun nimesi on?");

document.querySelector("#target").innerHTML =
    "Hei, " + nimi + "!";