const pesquisa = document.querySelector('.pesquisa-text');

pesquisa.addEventListener('input', (event) => {

    const searchValue = formatacao(event.target.value); 

    console.log(searchValue); 

    const items = document.querySelectorAll('.produto');

    items.forEach(item => {

        const itemText = formatacao(item.textContent);

        if (itemText.indexOf(searchValue) !== -1) {
            item.style.display = 'flex';
        } else {
            item.style.display = 'none';
        }
    });
});

function formatacao(value) {
    return value
        .toLowerCase()
        .trim();
}