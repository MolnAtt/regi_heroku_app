document.addEventListener("DOMContentLoaded", main);

function main(){
    document.getElementsByClassName('submitter')[0].addEventListener('click', kuld);
}


function kuld(e){
    document.getElementsByTagName('form')[0].submit();
}