const botao = document.getElementById("botao")
const msg = document.getElementById("mensagem")
const opcoes = document.querySelectorAll("li a")
const endereco = document.querySelector("p")

botao.addEventListener('click', function(){
	if (botao.innerText === "Portugues") {
		alert("A página agora está em Português.")
		msg.innerText = "Uma ração especial, para um amigo fantástico"
		opcoes[0].innerText = "Início"
		opcoes[1].innerText = "Destaque"
		opcoes[2].innerText = "Catálogo"
		endereco.innerText = "Avenida Akhanara, 123 / Tel: 91234-5678"		
		botao.innerText = "English"
	} else {
		alert("The website is now in English.")
		msg.innerText = "A special food for a fantastic friend!"
		opcoes[0].innerText = "Home"
		opcoes[1].innerText = "Highlight"
		opcoes[2].innerText = "Catalog"
		opcoes[0].href = "#"
		opcoes[1].href = "destaque.html"
        opcoes[2].href = "catalogo.html"
		botao.innerText = "Portugues"
		endereco.innerText = "Akhabara Avenue, 123 / Phone: 91234-5678"	
	}
})

