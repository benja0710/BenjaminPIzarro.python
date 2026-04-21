# explicacion y uso de for

# for i in range (7)
# print("hola")

# nom=int(input("ingrese un numero: "))
# for i in range (nom):
#     print("repeticion numero: ", i +1)
# print( "segunda forma")
# for i in range (1,nom+1):
#     print("repeticion numero: ", i)

# num=int(input("ingrese un numero: "))
# for i in range(12):
#     print(num, "x", i+1, "=", num*(i+1))
#     #segunda forma
#     print(f"{num} x {i+1} = {num*(i+1)} ")    


# titulo="clima de hoy"
# diadelmes=17
# mes=4
# tem=25.7
# llueve=False
# print("el", titulo, "es el dia", diadelmes, "del mes", mes, "con una temperatura de", tem, "grados y llueve:", llueve)  
# print(f"el {titulo} es el dia {diadelmes} del mes {mes} con una temperatura de {tem} grados y llueve: {llueve}")

# # tem>28 ----> False
# # mes==4 ----> True

# if llueve:
#     print("llevar paraguas")    
#     else:
#         print("no llevar paraguas")


#preguntar cuantas notas son y sacar el promedio
# num=int(input("ingrese la cantidad de notas: "))
# suma=0
# for i in range(num):
#     nota=float(input(f"ingrese la nota {i+1}: "))
#     suma += nota
# promedio=suma/num if num > 0 else 0
# print(f"el promedio es: {promedio}")

# total=0
# cantnotas=int(input("ingrese la cantidad de notas: "))
# for i in range(cantnotas):
#     nota=float(input(f"ingrese la nota {i+1}: "))
#     total = total + nota
# promedio=total/cantnotas 
# print(f"el promedio es: {promedio}")

# if promedio >= 4:
#     print("aprobado")       
# else:    print("reprobado")



# #sumatoria
# num=int(input("ingrese un numero: "))
# suma=0        
# for i in range(num):
#     suma = suma + i+1
# print("la sumatoria es: ", suma)

# #fctorial
# num=int(input("ingrese un numero: "))
# suma=1        
# for i in range(num):
#     suma = suma * (i+1)
# print("el factorial es: ", suma)



# for i in "benja":
#     print(i)
# conso=0
# cont=0
# vocales=0
# nombre=input("deme su nommbre: ")
# for i in nombre:
#     print(i)
#     if i in "aeiouAEIOU":
#         vocales=vocales+1
#         cont=cont+1
        
#         print(f"la palabra {nombre} tiene {vocales} vocales")
#         print(f"la cantidad de letras es: {cont}")
#     else:  
#         conso=conso+1 
#         print("el total de consonantes es: ", conso)
        
#         # if i=="a" or i== "e" or i=="i" or i=="o" or i=="u":



