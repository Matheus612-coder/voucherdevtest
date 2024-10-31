let botao = document.getElementById("botao")
let novoelemento = document.createElement("p")

botao.addEventListener("click", function(){
    
    novoelemento.innerHTML="Fui clicado"

    let botao2 = document.getElementsByTagName("body")

    botao2[0].appendChild(novoelemento)
    console.log("Fui clicado")

})
















