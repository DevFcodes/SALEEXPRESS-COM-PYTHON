const loginV = document.querySelector(".login__vendedor");
const loginVForm = document.querySelector(".loginV__form");

const venderProduto = document.querySelector(".vender__produto");

const handleLoginVendedor = (event) => {

    event.preventDefault();

    loginV.style.display = "none";
    venderProduto.style.display = "flex";
}

loginVForm.addEventListener("submit", handleLoginVendedor);





//adicionar imagem

const fileInput = document.getElementById('file-input');
const imgPreview = document.getElementById('image-preview');
const placeholder = document.getElementById('placeholder-text');

fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        if (!file.type.startsWith('image/')) {
            alert('Por favor, selecione um arquivo de imagem válido.');
            imgPreview.style.display = 'none';
            placeholder.style.display = 'block';
            return;
        }

        const reader = new FileReader();

        reader.onload = function(e) {
            imgPreview.src = e.target.result;
            
            imgPreview.style.display = 'block';
            placeholder.style.display = 'none';
        };

        reader.readAsDataURL(file);
    } else {
        imgPreview.style.display = 'none';
        imgPreview.src = '#';
        placeholder.style.display = 'block';
    }
});