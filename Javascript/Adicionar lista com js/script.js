let botao = document.getElementById("botao")
let entrada = document.getElementById("entrada")
let lista= document.getElementById("lista")



let elemento=document.getElementsByName("div")

botao.addEventListener("click", function(){

    let novoElemento = document.createElement("li")
    novoElemento.innerHTML=entrada.value
    lista.appendChild(novoElemento)    

    let botao2=document.createElement("button")
    botao2.innerHTML="Remover"
    novoElemento.appendChild(botao2)
      
    botao2.addEventListener("click", function(){

        novoElemento.remove()




    })

    
})



