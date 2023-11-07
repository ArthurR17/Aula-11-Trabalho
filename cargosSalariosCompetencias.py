print("-" * 150)
print("-" * 55 + "%0sRH 360 - CARGOS E SALÁRIOS - PETPALLET " % " " + "-" * 55)

cargos = {
    "1": [" Cargo: Atendente de Loja", "Competências:\n - Excelente atendimento ao cliente.\n - Conhecimento de produtos para animais de estimação.\n - Habilidade de vendas.\n - Organização da loja."," Salário: R$ 2.000,00"],
    "2": [" Cargo: Tosador de Animais", "Competências:\n - Habilidade de tosa e banho em cães e gatos.\n - Cuidado com a higiene e bem-estar dos animais.\n - Corte de unhas e limpeza de ouvidos."," Salário: R$ 3.000,00"],
    "3": [" Cargo: Auxiliar de Veterinário", "Competências:\n - Auxílio em procedimentos médicos.\n - Administração de medicamentos.\n - Cuidado com animais internados.\n - Agendamento de consultas."," Salário: R$ 2.500,00"],
    "4": [" Cargo: Gerente de Loja", "Competências:\n - Gerenciamento das operações da loja.\n - Supervisão da equipe. - Controle de estoque.\n - Pedidos de produtos.\n - Questões administrativas."," Salário: R$ 4.500,00"],
    "5": [" Cargo: Veterinário: ", "Competências:\n - Prestação de cuidados médicos a animais de estimação.\n - Realização de cirurgias.\n - Diagnóstico de doenças.\n - Vacinações. - Orientação a proprietários de animais.","Salário: R$ 10.000,00"],
    "6": [" Cargo: Banhista e Ajudante de Tosador", "Competências:\n - Auxílio em banhos, secagem e tosa.\n - Limpeza e esterilização do ambiente", "Salário: R$ 1.800,00"],
    "7": [" Cargo: Recepcionista", "Competêcias:\n - Recebimento de clientes.\n - Agendamento de consultas.\n - Atendimento telefônico.\n - Gerenciamento da agenda.\n - Informações sobre serviços e preços.", "Salário: 2.200,00"]
}


def tabelaCargos():
    print("-" * 150)
    print("%1sCÓDIGO" % " ", "%20sCARGO" % " ", "%33sCOMPETÊNCIAS" % " ", "%50sSALÁRIO" % " ")
    print("-" * 150)

    print("%3s1" % " ", "%19sAtendente de Loja" % " ", f"%13s - Excelente atendimento ao cliente." % " ",
          "%35s R$ 2.000,00\n" % " ", "%54s - Conhecimento de produtos para animais de estimação.\n" % " ",
          "%54s - Habilidadeidade vendas Organização loja.\n" % " ", "%54s - Organização.\n\n" % " ")

    print("%3s2" % " ", "%19sTosador de Animais" % " ", f"%12s - Habilidade de tosa e banho em cães e gatos." % " ",
          "%25s R$ 3.000,00\n" % " ", "%54s - Cuidado com a higiene e bem-estar dos animais.\n" % " ",
          "%54s - Corte de unhas e limpeza de ouvidos.\n\n" % " ")

    print("%3s3" % " ", "%19sAuxiliar de Veterinário" % " ", f"%7s - Auxílio em procedimentos médicos." % " ",
          "%35s R$ 2.500,00\n" % " ", "%54s - Administração de medicamentos.\n" % " ",
          "%54s - Cuidado com animais internados.\n" % " ", "%54s - Agendamento de consultas.\n\n" % " ")

    print("%3s4" % " ", "%19sGerente de Loja" % " ", f"%15s - Gerenciamento das operações da loja." % " ",
          "%32s R$ 4.500,00\n" % " ", "%54s - Supervisão da equipe.\n" % " ", "%54s - Controle de estoque.\n" % " ",
          "%54s - Pedidos de produtos.\n" % " ", "%54s - Questões administrativas.\n\n" % " ")

    print("%3s5" % " ", "%19sVeterinário" % " ",
          f"%19s - Prestação de cuidados médicos a animais de estimação." % " ", "%15s R$ 10.000,00\n" % " ",
          "%54s - Realização de cirurgias.\n" % " ", "%54s - Diagnóstico de doenças.\n" % " ",
          "%54s - Vacinações.\n" % " ", "%54s - Orientação a proprietários de animais.\n\n" % " ")

    print("%3s6" % " ", "%19sBanhista e Ajudante de Tosador" % " ",
          f"%0s - Auxílio em banhos, secagem e tosa." % " ", "%33s R$ 1.800,00\n" % " ",
          "%55s - Limpeza e esterilização do ambiente.\n\n" % " ")

    print("%3s7" % " ", "%19sRecepcionista" % " ", f"%17s - Recebimento de clientes." % " ",
          "%44s R$ 2.200,00\n" % " ", "%54s - Agendamento de consultas.\n" % " ",
          "%54s - Atendimento telefônico.\n" % " ", "%54s - Gerenciamento da agenda.\n" % " ",
          "%54s - Informações sobre serviços e preços.\n" % "")
    print("-" * 150)


tabelaCargos()

while True:
    print("\nMenu de opções: ")
    print("1 - Pesquisar código")
    print("2 - Listar todos os cargos")
    print("3 - Sair")
    opcao = input("Escoha uma opção: ")

    if opcao == "1":
        codigo = input("Digite o código do cargo: ")
        if codigo in cargos:
            print(f"\n{cargos[codigo][0]}\n {cargos[codigo][1]}\n {cargos[codigo][2]}")
    elif opcao == "2":
        tabelaCargos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida")
