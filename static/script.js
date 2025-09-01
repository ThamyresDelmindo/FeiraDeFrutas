function clickfuncao(){
  let select = document.querySelector(".frutas")
  let value = select.value

  const frutas = ["Banana", "Maçã", "Laranja", "Uva", "Morango", "Abacaxi", "Manga", "Pera", "Melancia", "Kiwi" ];


  if (value == "Ver tudo") {
    alert("Frutas disponíveis: " + frutas.join(", "))
  }
  else if (value == "Adicionar") {
      let fruta_adicionada = prompt("Digite o nome da fruta que deseja adicionar: ")
      frutas.push(fruta_adicionada)
      alert(fruta_adicionada + " foi adicionada ao Menu")
  }
      
  else if (value == "Remover") {
    let fruta_removida = prompt("Digite o nome da fruta que deseja remover: ")
    let posicao = frutas.indexOf(fruta_removida)  /* procura a fruta para o splice remover depois */
    if (posicao !== -1) {
      frutas.splice(posicao, 1)
      alert(fruta_removida + "foi removida do Menu")
    } else {
      alert(fruta_removida + "não existe no Menu")
    }
  }

  else if (value == "Consultar") {
    let fruta_consulta = prompt("Digite o nome da fruta que deseja consultar: ")
    let posicao = frutas.indexOf(fruta_consulta)
    if (posicao != -1) {
      alert(fruta_consulta + "está disponível no Menu")
    } else {
      alert(fruta_consulta + "não existe no Menu")
    }
  }

  else if (value == "Quantidade") {
    let quantidade = frutas.length
    alert("Há" + quantidade + "frutas no Menu")
  } 

  else if (value == "Editar") {
    let fruta_a_editar = prompt("Digite o nome da fruta que deseja editar")
    let posicao = frutas.indexOf(fruta_a_editar)
    if (posicao != -1) {
      alert(fruta_a_editar + "está disponível no Menu")
      let fruta_editada = prompt("Digite o novo nome para essa fruta")
      frutas[posicao] = fruta_editada
      alert(fruta_editada + "foi atualizada no Menu")
    }
  }

}
