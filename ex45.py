def numeros(x, y):
    if x > y:
     return x 
    else:
     return y
# interação com o usuário
n1 = int(input("Digite primeiro número "))
n2 = int(input("Digite segundo número "))
# chamada da função e exibição do resultado maior_numero = maior(n1, n2)
maior_numero = numeros(n1, n2)          
print(f"O maior número entre {n1} e {n2} é: {maior_numero}")

