anonasc = int(input("digitando o ano de nascimento"))
genero = input("digite seu genero M ou f ").upper()
print(anonasc)
print(genero)
idade=2025-anonasc
if (idade >= 18 and genero == "M"):
    print ("Apto a se alistar")
else:
        print ("Não apto")

