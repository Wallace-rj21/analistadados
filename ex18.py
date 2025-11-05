prod=input("Digite um produto").upper()
if (prod=="MOUSE"):
    preco=10
elif (prod=="TECLADO"):
    preco=20
elif (prod=="MEMÓRIA"):
    preco=100
else:
    preco=0   
    print("produto não existente")
qtd= int(input("digite a quantidade"))
prodtotal= preco * qtd
if (preco > 10):
    imposto = prodtotal * 0.05
else:
    imposto = prodtotal * 0.1
valorfinal= prodtotal + imposto
print (f"seu produto é {prod}")
print (f" imposto {imposto}")
print (f" valor final é {valorfinal}")
