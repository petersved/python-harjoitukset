"use strict";

const vuosiluku = Number(prompt("Anna vuosiluku"));

if (vuosiluku % 400 == 0) {
    document.getElementById("target").innerHTML =
        vuosiluku + " on karkausvuosi.";
}

else if (vuosiluku % 100 == 0) {
    document.getElementById("target").innerHTML = 
        vuosiluku + " ei ole karkausvuosi.";
}

else if (vuosiluku % 4 == 0) {
    document.getElementById("target").innerHTML = 
        vuosiluku + " on karkausvuosi.";
}

else {
    document.getElementById("target").innerHTML = 
        vuosiluku + " ei ole karkausvuosi.";
}






