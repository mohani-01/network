
document.addEventListener('DOMContentLoaded', () => {
    loadFirstPage();


    document.querySelector('#form-post').addEventListener('click', () => newPost());
});
// Things need to be done when page first load
function loadFirstPage() {
    document.querySelector('#input-post').disabled = true;
}


function newPost() {

    document.querySelector('#text-post').onkeyup = () =>  { 
        if (document.querySelector('#text-post').value.trim().length > 0 ) {

            document.querySelector('#input-post').disabled = false;
        } else {
            document.querySelector('#input-post').disabled = true;
        }
    }
}