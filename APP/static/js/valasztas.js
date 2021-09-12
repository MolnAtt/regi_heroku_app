document.addEventListener("DOMContentLoaded", main);

function main(){
    //    console.log("betöltött a DOM");
    for (const gomb of document.getElementsByClassName('gomb')) {
        gomb.addEventListener('click', kuld);
    }

    //    console.log("hibaüzenetek kiírása");
    for (const uzenet of uzenetek) { alert(uzenet); }

}

function kuld(e){
    e.target.parentNode.children[7].value = e.target.classList.value.split(' ').slice(-1)[0];
    e.target.parentNode.submit();
}

