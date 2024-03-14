#este lleva if y else
print("Este teatro solo acepta gente mayor a 5 años que edad tiene usted?\n")
edad=int(input("Recuerde niños menores a 5 años no entran \n"))

if edad>=5:
    if edad<=14 and edad>=5 or edad>=66:
        print("su descuento es del 35%")
    elif edad<=19 and edad>=15 or edad<=65 and edad>=46:
        print("tu descuento es de 25%")
    elif edad<=45 and edad>=20:
        print("tu descuento es del 10%")
else:
    if edad<5 and edad>=0:
        print("Lo siento no se aceptan niños")
    else:
        print("Su bebe aun no nace? su numero es negativo")

print("Fin del programa")