soma_positivos = 0
numero = -1 # Inicializa com um valor diferente de 0 para entrar no loop
while numero != 0:
#pede o número e converte para inteiro
    entrada = input("Digite um número (0 para parar): ")
try:
    numero = int(entrada)
except ValueError:
    print("Entrada inválida. Digite um número inteiro")
continue # Volta para início do loop
# usa o if para verificar se o número é positivo antes de somar
if numero >0:
    soma_positivo = soma_positivos + numero
print(f"A soma dos números positivos digitados é: {soma_positivos}")