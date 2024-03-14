#una empresa de bienes raices ofrece casas de.... sobre 80000 se da un pie bajo 80000 otro

llave=True
pie_y_años=[]

while llave==True:


    ingresos=int(input("Cuanto es su ingreso?\n"))
    if ingresos>80000:
        print("Su pie debe ser del 15% de la casa\n el resto se distribuira en pagos mensuales durante los proximos 10 años")

        pie_y_años.append("Pie: 15% y 10 años")
    elif ingresos<80000 and ingresos>0:
        print("Su pie debe ser del 30% de la casa\n el resto se distribuira en pagos mensuales durante los proximos 7 años")

        pie_y_años.append("Pie: 30% y 7 años")
    elif ingresos<=0:
        print("tiene que tener al menos algo de ingresos")
    x=int(input("desea continuar? 1 para continuar\n"))
    if x==1:
        llave=True
    else:
        llave=False

print(pie_y_años)


