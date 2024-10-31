let botao = document.getElementById("botao")
let novoelemento=document.createElement("p")
soma = 0

botao.addEventListener("click", function(){
    novoelemento.innerHTML="Cliques:"+ soma

    let botao2 = document.getElementsByTagName("body")
    botao2[0].appendChild(novoelemento)
    soma++
})


