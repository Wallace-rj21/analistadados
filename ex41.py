def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def mult(a, b):
    return a * b

def divi(a, b):
    if b !=0:
      return a/b
    else:
      print("valor inválido")
escolha = ""
while escolha != "0":
    escolha = input("Digite uma opção 0-parar, 1-somar, 2-subtrair, 3-multi, 4-divi")
    num1= int(input("Digite o primeiro número"))
    num2= int(input("Digite o primeiro número"))
    if escolha == "1":
        x=somar(num1, num2)
    elif escolha == "2":
        x=subtrair(num1, num2)
    elif escolha == "3":
        x=mult(num1, num2)
    elif escolha == "4":
        x=divi(num1, num2)
    elif escolha == "0":
        break
print(f"Resultado da operação: {x}")
