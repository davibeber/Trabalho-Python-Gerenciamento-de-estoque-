from datetime import datetime

historico=[]
armazem = [
    {"id": 101, "nome": "Monitor", "qnt": 10},
    {"id": 102, "nome": "Teclado", "qnt": 30},
    {"id": 103, "nome": "Mouse", "qnt": 5},
]

# Sobre os IDs não é possivel iniciar números "int" com zero por causa da base octal (base 8)
# ou eu alterava o id para um int aceitavel ou considerava os numeros como string "001"

def adicionar_item():
    while True:
        try: #try/catch: script de prevenção de erro.
            novo_nome = input("Qual o nome do item do estoque?")
        except:
            print("ERROR, tente novamente")
        while True:
            try:
                nova_qnt = int(input("Qual a quantidade do item do estoque?"))
                break
            except:
                print("ERROR, tente novamente")

novo_id = 101 + len(armazem)
novo_item = {"id": novo_id, "nome": novo_nome, "qnt": nova_qnt}
print(novo_item)
armazem.append(novo_item)
agora = datetime.now()
data_adicao = agora.strftime("%d/%m/%Y %H:%M")

registro={
    "data": data_adicao,
    "id": novo_id,
    "nome":novo_nome,
    "qnt": novo_qnt,
}
historico.append(registro)


def remover_item():
    nome = input("Qual o nome do item que deseja remover?")
    qnt = int(input("Qual a quantidade?"))

for b in armazem:
    if b["nome"] == nome:
        if b["qnt"] >=qnt:
            b["qnt"] -= qnt
        print(f"Concluido! Item {b['nome']} com estoque de {b['qnt']}")

        agora = datetime.now()
        data_remocao = agora.strftime("%d/%m/%Y %H:%M")

        registro={
            "data": data_remocao,
            "id": b["id"],
            "nome": b["nome"],
            "qnt": b["qnt"],
        }
        historico.append(registro)

    else:
        if b["qnt"] ==0:
            print("ERROR, estoque vazio")
        else:
            print("quantidade insuficiente")


def exibir_armazem():
    for a in armazem:
        print(f"id: {a["id"]}, Nome: {a["nome"]}, Qnt: {a["qnt"]}")


def exibir_historico():
    if not historico:
        print("historico vazio")
    for reg in historico:
        print(f"{reg['data']} | {reg['tipo']} | Item: {reg['produto']} | Qtd: {reg['qtd']}")
while True:
    print("opções")
    print("1-adicionar item ao estoque")
    print("2-remover item do estoque")
    print("3-exibir lista do estoque")
    print("4-exibir historico do estoque")
    print("5-sair")

    item=input(print("Qual a sua escolha?"))

    match item :
        case "1" :
            adicionar_item()
        case "2":
            remover_item()
        case "3" :
            exibir_armazem()
        case "4":
            exibir_historico()
        case "5":
            print("Saindo do estoque")
    break








