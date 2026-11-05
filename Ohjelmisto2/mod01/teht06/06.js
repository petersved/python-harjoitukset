"use strict";

const laske = confirm("Lasketaanko neliö?")

if (laske == true) {
    const luku = Number(prompt("Anna luku: "));
    
    if (luku < 0) {
        document.getElementById("target").innerHTML =
            "Negatiivisen luvun neliöjuurta ei ole määritelty.";

    }

    
    else {
    
        const neliöjuuri = Math.sqrt(luku); 

        document.getElementById("target").innerHTML =
            "Luvun " + luku + " neliöjuuri on " + neliöjuuri;
    }
}    
else { 
    document.getElementById("target").innerHTML = 
        "Neliöjuurta ei lasketa"
}


    




