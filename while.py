# uso y explicacion de while
# cont=0
# while cont<10:
#     print("repeticion",cont)
#     cont+=1

# pin=1234
# ingreso=int(input("ingrese su pin: "))
# while ingreso!=pin:
#     print("pin incorrecto")
#     ingreso=int(input("ingrese su pin: "))
# print("pin correcto")



# op=0
# total=0
# while op!=4:
#     print("1.- xbox series x 250.000")
#     print("2.- playstation 5 500.000")
#     print("3.- nintendo switch 300.000")
#     print("4.- salir")
#     opcion = int(input("seleccione una opcion: "))
#     match opcion:
#     case 1:
#         print("el valor a pagar ", 250000*1.19)
#         total+=250000*1.19
#     case 2:
#         print("el valor a pagar ", 500000*1.19)
#         total+=500000*1.19
#     case 3:
#         print("el valor a pagar ", 300000*1.19)
#         total+=300000*1.19
#     case 4:
#         print("el total a pagar es: ", total)
#     case _:
#         print("opcion no valida")





# crear calculadora +, -, *, / y salir. Preguntar por la operacion a realizar y luego por los numeros. Mostrar el resultado. Repetir hasta que se seleccione salir  
op=0
while op!=5:
    print("1.- suma")
    print("2.- resta")
    print("3.- multiplicacion")
    print("4.- division")
    print("5.- salir")
    opcion = int(input("seleccione una opcion: "))
    if opcion in [1,2,3,4]:
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))
        if opcion == 1:
            print("el resultado es: ", num1+num2)
        elif opcion == 2:
            print("el resultado es: ", num1-num2)
        elif opcion == 3:
            print("el resultado es: ", num1*num2)
        elif opcion == 4:
            if num2 != 0:
                print("el resultado es: ", num1/num2)
            else:
                print("error: division por cero")
    elif opcion == 5:
        print("saliendo de la calculadora...")
    else:
        print("opcion no valida")
 





