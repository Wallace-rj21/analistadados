v1=float(input("primeiro valor"))
v2=float(input("segundo valor"))
v3=float(input("terceiro valor"))
if ( v1 > v2 and v1 > v3):
    print(f"{v1} é maior do que {v2} {v3}")
elif ( v2 > v1 and v2 > v3 ):
    print(f"{v2} é maior que {v3} {v1}")
else:
    print (f"{v3} é maior que {v1} {v2}")