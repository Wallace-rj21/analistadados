a1=float(input("digite uma nota"))
a2=float(input("digite uma outra nota "))
a3=float(input("digite mais uma outra nota "))
a4=float(input("digite a última nota "))
media = (a1+a2+a3+a4)/4
if (media >= 6):
    print (f"aprovado {media}")
else:
    print (f"reprovado {media}")