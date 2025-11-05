t1=float(input("digite uma temperatura"))
if ( t1 < 18 ):
    print (f"{t1} está frio pois está menor do que 18 graus")
elif ( t1 > 18 and t1 <= 24 ):
    print (f"{t1} está agradável pois está igual ou maior do que 18 até 24 graus")
else:
    print (f"{t1} está calor por ser maior do que 24")