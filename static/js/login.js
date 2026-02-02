
function validarCPF(cpf) {
    const reFormat = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
    const reDigits = /^\d{11}$/;
    return reFormat.test(cpf) || reDigits.test(cpf);
}

function fazerLogin() {
    console.log("Função fazerLogin chamada!"); // DEBUG

    const resultado = document.getElementById("resultado");
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value;
    const cpf = document.getElementById("cpf").value.trim();
    const lembrar = document.getElementById("lembrar").checked;

    console.log("Dados:", { email, cpf, senha: "***" }); // DEBUG

    // Validações
    if (!email || !senha || !cpf) {
        resultado.textContent = "❌ Preencha todos os campos!";
        resultado.style.color = "red";
        return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        resultado.textContent = "❌ Email inválido!";
        resultado.style.color = "red";
        return;
    }

    if (!validarCPF(cpf)) {
        resultado.textContent = "❌ CPF inválido!";
        resultado.style.color = "red";
        return;
    }

    if (senha.length < 6) {
        resultado.textContent = "❌ Senha deve ter 6+ caracteres!";
        resultado.style.color = "red";
        return;
    }

    // Login OK
    const nome = email.split("@")[0];
    resultado.textContent = `✅ Login efetuado com sucesso!`;
    resultado.style.color = "#4caf50";

    if (lembrar) {
        localStorage.setItem("user_email", email);
        localStorage.setItem("user_nome", nome);
    }

    console.log("Redirecionando..."); // DEBUG

    setTimeout(() => {
        window.location.href = "catalogo.html";
    }, 1000);
}