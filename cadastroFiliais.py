print("-" * 150)
print("-" * 55 + "%0sRH 360 - CADASTRO FILIAIS - PETPALLET " % " " + "-" * 55)
print("-" * 150)


Filiais = {}

print("Opções: ")
print("1 - Cadastrar nova filial")
print("2 - Listar filiais")
print("3 - Sair")

while True:

    opcao = input("Escolha a opção desejada: ")
    if opcao == "1":
        nome = input("Digite o nome da filial: ")
        cidade = input("Digite a cidade da filial: ")
        endereco = input("Digite o endereço da filial: ")
        Telefone = input("Digite o telefone da filial: ")
        print(f"Filiado {nome} adicionado com sucesso")

        numero_filial = len(Filiais) + 1
        Filiais[str(numero_filial)] = {
            "Nome": nome,
            "Cidade": cidade,
            "Endereço": endereco,
            "Telefone": Telefone
        }

        print(f"Filial {numero_filial} adicionada com sucesso")
    elif opcao == "2":
        for numero, dados in Filiais.items():
            print(f"Filial {numero}:")
            print(f"Nome: {dados['Nome']} | Cidade: {dados['Cidade']} | Endereço: {dados['Endereço']} | Telefone: {dados['Telefone']}")

    elif opcao == "3":
        print("Processo encerrado")
        break
    else:
        print("Opção inválida")
