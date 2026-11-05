const nimi = prompt("Kerro nimesi");

const luku = Math.floor(Math.random() * 4) + 1;

if (luku == 1) {
    document.getElementById("target").innerHTML = 
        nimi + ", sinä olet rohkelikko.";
        
}

else if (luku == 2) {
    document.getElementById("target").innerHTML = 
        nimi + ", sinä olet luihunen."
}

else if (luku == 3) {
    document.getElementById("target").innerHTML =
        nimi + ", sinä olet puuskupuh."
}

else {
    document.getElementById("target").innerHTML =
        nimi + ", sinä olet korpinkynsi."
}