def saudar (nome):
    return f"olá, {nome}! Seja bem vindo ao mundo Python!"
nome_usuário = input("Digite seu nome: ")
mensagem = saudar(nome_usuário)
print(mensagem)