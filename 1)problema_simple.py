#EJERCICIO1
#Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero que el teatro
#deja de percibir por cada una de las categorías. Tomar en cuenta que los niños menores de 5 años
#no pueden entrar al teatro y que existe un precio único en los asientos. Los descuentos se hacen
#tomando en cuenta...

print("Este teatro solo acepta gente mayor a 5 años que edad tiene usted?\n")
edad=int(input("Recuerde niños menores a 5 años no entran \n"))

if edad>=5:
    if edad<=14 and edad>=5 or edad>=66:
        print("su descuento es del 35%")
    elif edad<=19 and edad>=15 or edad<=65 and edad>=46:
        print("tu descuento es de 25%")
    elif edad<=45 and edad>=20:
        print("tu descuento es del 10%")
    
print("Fin del programa")