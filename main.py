import json

def add_respostas(perguntas, respostas):
    nova_resposta = {}
    for pergunta in perguntas:
        resposta = input(pergunta + ": ")
        nova_resposta[pergunta] = resposta
    respostas.append(nova_resposta)

def salvar_no_json(respostas, filename):
    with open(filename, 'w') as file:
        json.dump(respostas, file)

def carregar_do_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    perguntas = ["Qual o seu nome?", "Qual a sua idade?", "Qual o seu emprego?"]
    filename = "respostas.json"
    respostas = carregar_do_json(filename)

    while True:
        print("Menu:")
        print("1) Adicionar respostas")
        print("2) Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            add_respostas(perguntas, respostas)
        elif opcao == '2':
            salvar_no_json(respostas, filename)
            print("Respostas salvas. Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()