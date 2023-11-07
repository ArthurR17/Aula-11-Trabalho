print("-" * 147)
print("-" * 50 + "%0sRH 360 - CADASTRO DE FUNCIONÁRIOS - PETPALLET " % " " + "-" * 50)
print("-" * 147)

contatos = {}

print("OPÇÕES: ")
print("1 - Cadastrar Funcionário")
print("2 - Pesquisar Funcionário")
print("3 - Lista de todos os Funcionários")
print("4 - Deslogar\n")

while True:
    opcao = input("ESCOLHA UMA DAS OPÇÕES: ")
    if opcao == "1":
        nome = input("Digite o NOME do funcionário: ")
        telefone = input("Digite o NÚMERO DE TELEFONE: ")
        cargo = input("Digite o CARGO: ")
        salario = input("Digite o SALÁRIO: ")
        email = input("Digite o EMAIL do funcionário: ")

        if nome in contatos and contatos[nome] == {"telefone": telefone, "cargo": cargo, "salario": salario, "email": email}:
            print(f"\nO FUNCIONÁRIO {nome} JÁ EXISTE NA AGENDA.\n")
        else:
            contatos[nome] = {"telefone": telefone, "cargo": cargo, "salario": salario, "email": email}
            print(f"\nFUNCIONÁRIO(A) {nome} CADASTRADO(A) COM SUCESSO !! \n")

    elif opcao == "2":
        nome = input("\nDigite o nome do funcionário a ser pesquisado: \n")
        if nome in contatos:
            print(f"\nNome (funcionário): {nome}")
            print(f"Telefone (funcionário): {contatos[nome]['telefone']}")
            print(f"Cargo (funcionário): {contatos[nome]['cargo']}")
            print(f"Salario (funcionário): R${contatos[nome]['salario']}")
            print(f"Email (funcionário): {contatos[nome]['email']}\n")

        else:
            print(f"\nCADASTRO DE NOME: {nome} NÃO ENCONTRADO !!\n")

    elif opcao == "3":
        if not contatos:
            print("Não existem funcionários cadastrados.")
        else:
            for nome, info in contatos.items():
                print(f"\n| Nome: {nome} \n| Telefone: {info['telefone']} \n| Cargo: {info['cargo']} \n| Salario: R${info['salario']} \n| Email: {info['email']}\n")
    elif opcao == "4":
        print("Processo finalizado")
        break
