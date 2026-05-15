# op=0
# total=0
# while True:
#     print("1.- PC $500.000")
#     print("2.- LGTV 55 pulgadas $450.000")
#     print("3.- Microondas Mademsa $100.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print("El total a pagar es ",500000*1.19 )
#             total+=500000*1.19
#         case 2:
#             print("El total a pagar es ",450000*1.19 )
#             total+=450000*1.19
#         case 3:
#             print("El total a pagar es ",100000*1.19 )
#             total+=100000*1.19
#         case 4:
#             break
#             print("Saliendo")
#             print("El total a pagar es", total)
#         case _:
#             print("Opción inválida")







# Pedir al usuario la cantidad d notas 
# mostrar el premedio de ellas
# determinar si el alumno aprueba o no
while True:
    try:
        notas=int(input("Ingrese la cant de notas: "))
        suma=0
        break
    except:
        print("Solo numeros enteros")
for i in range(notas):
    n=float(input(f"Ingrese la nota {i+1}: "))
    suma=suma+n
    # suma+=n
prom=suma/notas
print("El promedio es",round(prom,1) )

if prom>=4:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")