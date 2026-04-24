# uso y explicaciones de match

# print("1.- opcion 1")
# print("2.- opcion 2")
# print("3.- opcion 3")
# opcion = int(input("seleccione una opcion: "))
# match opcion:
#     case 1:
#         print("ha seleccionado la opcion 1")
#     case 2:
#         print("ha seleccionado la opcion 2")
#     case 3:
#         print("ha seleccionado la opcion 3")
#     case _:
#         print("opcion no valida")




print("1.- xbox series x 250.000")
print("2.- playstation 5 500.000")
print("3.- nintendo switch 300.000")
opcion = int(input("seleccione una opcion: "))
match opcion:
    case 1:
        print("el valor a pagar ", 250000*1.19)
    case 2:
        print("el valor a pagar ", 500000*1.19)
    case 3:
        print("el valor a pagar ", 300000*1.19)
    case _:
        print("opcion no valida")