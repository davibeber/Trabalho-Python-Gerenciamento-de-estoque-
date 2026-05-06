from datetime import datetime

historico=[]
estoque=[
    {"id":101, "nome":"monitor", "quantidade":30},
    {"id":102, "nome":"teclado", "quantidade":40},
    {"id":103, "nome":"mouse", "quantidade":20},
]

# Sistema de login para identificação do responsavel na reposição do estoque
print("--- SISTEMA DE ESTOQUE ---")
while True:
    responsavel=input("Nome: ")
    senha=input("Senha(1234): ")
    if senha=="1234":
        print(f"Bem-vindo, {responsavel}!")
        break
    else:
        print("ERRO: Senha incorreta, tente novamente.")

def adicionar_item():
    while True:
        nome_adicionado=input("Qual o nome do item do estoque?")
        if not nome_adicionado.replace(" ", "").isalpha():
            # .isalpha() valida se o dado fornecido é composto apenas por letras.
            # O "not" inverte o resultado, então entra no if quando NÃO for apenas letras.
            print("ERRO: O nome deve conter apenas letras.")
            continue

        while True:
            entrada_qnt=input(f"Qual a quantidade de {nome_adicionado}?")
            if entrada_qnt.isdigit():
                # .isdigit() valida se o dado fornecido é composto apenas por números.
                # Caso não seja, o else exibe a mensagem de erro e repete o loop.
                v_qnt=int(entrada_qnt)
                break
            else:
                print("ERRO: A quantidade deve ser um número.")

        novo_nome=nome_adicionado.lower()
        # uso de .lower() para conversão das letras dos nomes para minúsculas

        # verifica se o item já existe no estoque
        item_existente=None
        for b in estoque:
            if b["nome"]==novo_nome:
                item_existente=b
                break

        if item_existente:
            # se existe, soma a quantidade
            item_existente["quantidade"]+=v_qnt
            print(f"Item já existente! Quantidade atualizada para {item_existente['quantidade']}.")
        else:
            # se não existe, adiciona normalmente
            novo_id=101 + len(estoque)
            novo_item={"id":novo_id, "nome":novo_nome, "quantidade":v_qnt}
            estoque.append(novo_item)


        #Dicionario para organizar dados na lista "historico"
        registro={
            "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "tipo": "ENTRADA",
            "nome": novo_nome,
            "quantidade": v_qnt,
            "responsavel": responsavel
        }
        historico.append(registro)#adicionar o registro na lista "historico"
        print(f"Item {novo_nome} adicionado/atualizado com sucesso!")
        break


def remover_item():
    nome_procurado=input("Qual o nome do item que deseja remover? ")
    while True:
        qtd_entrada=input(f"Quanto de '{nome_procurado}' deseja retirar? ")
        if qtd_entrada.isdigit():
            v_remover=int(qtd_entrada)
            break
        else:
            print("ERRO: Digite um número inteiro.")

    achado=False
    for b in estoque:
        if b["nome"].lower()==nome_procurado.lower():
            achado=True

            # Se a quantidade que tem disponivel for maior do que foi requisitado, subtrai
            if b["quantidade"]>=v_remover:
                b["quantidade"]-=v_remover
                print(f"Concluído! Item {b['nome']} agora tem {b['quantidade']} no estoque.")

                registro={
                    "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "tipo": "SAÍDA",
                    "nome": b["nome"],
                    "quantidade": v_remover,
                    "responsavel": responsavel
                }
                historico.append(registro)
            else:
                print(f"ERRO: Insuficiente. Disponibilidade atual: {b['quantidade']}")
            return

    if not achado:
        print("ERRO: Produto não encontrado.")


def exibir_estoque():
    print("--- ESTOQUE ATUAL ---")
    for a in estoque:
        print(f"ID: {a['id']} | Nome: {a['nome']} | quantidade: {a['quantidade']}")

def exibir_historico():
    print("--- HISTÓRICO ---")
    if not historico:
        print("Histórico vazio.")
    else:
        for reg in historico:
            print(f"{reg['data']} | {reg['tipo']} | Item: {reg['nome']} | quantidade: {reg['quantidade']} | Responsável: {reg['responsavel']}")


# Menu principal
while True:
    print("--- MENU PRINCIPAL ---")
    print("O que voce deseja?")
    print("1 - Adicionar item ao estoque")
    print("2 - Retirar item do estoque")
    print("3 - Visualizar estoque atual")
    print("4 - Visualizar historico")
    print("5 - Sair")
    escolha=input("Qual a sua escolha?")

    if escolha=="1":
        adicionar_item()
    elif escolha=="2":
        remover_item()
    elif escolha=="3":
        exibir_estoque()
    elif escolha=="4":
        exibir_historico()
    elif escolha=="5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")