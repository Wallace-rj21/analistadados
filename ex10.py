valor1=int(input("digite primeiro valor"))
valor2=int(input("digite segundo valor"))
if ( valor1 > valor2 ):
    print (f"{valor1} maior do que {valor2}")
elif ( valor2 > valor1 ):
    print (f"{valor2} maior do que {valor1}")
else:
    print (f"são iguais")