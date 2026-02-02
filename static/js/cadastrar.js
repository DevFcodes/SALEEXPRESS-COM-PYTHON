document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("cadastroForm");
  const resultado = document.getElementById("resultado");

  function showMsg(msg, ok = false) {
    resultado.textContent = msg;
    resultado.style.color = ok ? "green" : "red";
  }

  function validarCPF(cpf) {
    const reFormat = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
    const reDigits = /^\d{11}$/;
    return reFormat.test(cpf) || reDigits.test(cpf);
  }

  function calcularIdade(dataNascimento) {
    const hoje = new Date();
    const nascimento = new Date(dataNascimento);
    let idade = hoje.getFullYear() - nascimento.getFullYear();
    const mes = hoje.getMonth() - nascimento.getMonth();
    
    if (mes < 0 || (mes === 0 && hoje.getDate() < nascimento.getDate())) {
      idade--;
    }
    
    return idade;
  }

  form.addEventListener("submit", function (event) {
    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value;
    const data = document.getElementById("data").value;
    const endereco = document.getElementById("endereco").value.trim();
    const cpf = document.getElementById("cpf").value.trim();

    resultado.textContent = "";

    // Validação de campos vazios
    if (!nome || !email || !senha || !data || !endereco || !cpf) {
      event.preventDefault();
      showMsg("Preencha todos os campos.");
      return;
    }

    const idade = calcularIdade(data);
    const anoNascimento = new Date(data).getFullYear();

    if (idade < 18) {
      event.preventDefault();
      showMsg("Você precisa ter 18 anos ou mais.");
      return;
    }

    if (anoNascimento < 1930) {
      event.preventDefault();
      showMsg("Ano de nascimento inválido.");
      return;
    }

    if (senha.length < 4) {
      event.preventDefault();
      showMsg("A senha precisa ter no mínimo 4 caracteres.");
      return;
    } else if(senha === 1234){
      event.preventDefault()
      showMsg("Não é possivel deixar a senha como:  1234");
      return;
    }

    if (!validarCPF(cpf)) {
      event.preventDefault();
      showMsg("CPF inválido. Use formato:12345678900");
      return;
    }

    // Se chegou aqui → deixa o Flask receber
    showMsg("Dados válidos! Finalizando cadastro...", true);
  });
});