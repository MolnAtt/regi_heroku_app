document.addEventListener("DOMContentLoaded", main);

function main(){
//    console.log("betöltött a DOM");
    for (const gomb of document.getElementsByClassName('gomb')) {
        gomb.addEventListener('click', kuld);
    }
}

function kuld(e){
    e.target.parentNode.children[7].value = e.target.classList.value.split(' ').slice(-1)[0];
    e.target.parentNode.submit();
}

