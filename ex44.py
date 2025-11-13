def quadrado(lado):
    # Usando o operador de exponenciação (**)
    return lado ** 2
#Interação com o usuário 
medida_lado = float(input("Digite a medida do lado do quadrado: "))
#chamada da função e exibição do resultado
area = quadrado(medida_lado)
print (f"Area do quadrado é: {area}")
