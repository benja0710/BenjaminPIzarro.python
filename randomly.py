import random
import time
# uso y explicacion de random
# import random       
# num= random.randint(1,10)
# print(num)

# for i in range(num):
#     print("hola mundo")


# 3 personas juegan golf, cada persona tiene la posibilidad de golpear y la distancia varia entre 60 y 190 metros, mostrar al final el golpe mas fuerte 

# golp1 = random.randint(60,190)
# print (f"golpe 1: {golp1} metros")
# golp2 = random.randint(60,190)
# print (f"golpe 2: {golp2} metros")
# golp3 = random.randint(60,190)
# print (f"golpe 3: {golp3} metros")
# if golp1 > golp2 and golp1 > golp3:
#     print(f"el golpe mas fuerte es el golpe 1 con {golp1} metros")
# elif golp2 > golp1 and golp2 > golp3:
#     print(f"el golpe mas fuerte es el golpe 2 con {golp2} metros")
# else:
#     print(f"el golpe mas fuerte es el golpe 3 con {golp3} metros")

# tira 2 dados 
# dado1 = random.randint(1,6)
# dado2 = random.randint(1,6)
# print(f"dado 1: {dado1}")
# print(f"dado 2: {dado2}")
# print(f"suma: {dado1 + dado2}")
# time.sleep(2)
# # si los dados dan el mismo numero, el jugador gana
# if dado1 == dado2:
#     print("¡Felicidades! Has ganado.")
# else:    print("Lo siento, has perdido. Inténtalo de nuevo.")

#ludo
# 1 jugador juega y lanza 2 dados, por cada unidad en el dado avanza una posicion en el tablero, cuando llegue a 50 gana. Mostrar cuantos turnos le toma llegar a la meta.
# posicion = 0
# turnos = 0      
# while posicion < 50:
#     dado1 = random.randint(1,6)
#     dado2 = random.randint(1,6)
#     posicion += dado1 + dado2
#     turnos += 1
#     time.sleep(1)
#     print(f"Turno {turnos}: Avanzaste {dado1 + dado2} posiciones. Posición actual: {posicion}")
# print(f"¡Felicidades! Has llegado a la meta en {turnos} turnos.")


#dos peleadores se piden al inicio de la pelea, cada uno tiene una vida de 100 de HP, se debe hacer una pelea por turnos y cada golpe varia entre 7 y 18. Se termina el match cuando uno de los dos tiene su HP menor o igual a 0, se debe mostrar el ganador al final.
#Bonus: mostrar la barra de vida de cada peleador en cada turno.
# peleador1 = input("Ingrese el nombre del primer peleador: ")
# peleador2 = input("Ingrese el nombre del segundo peleador: ")
# hp1 = 100
# hp2 = 100
# turno = 1
# while hp1 > 0 and hp2 > 0:
#     print(f"\nTurno {turno}:")
#     golpe1 = random.randint(7,18)
#     golpe2 = random.randint(7,18)
#     hp2 -= golpe1
#     hp1 -= golpe2
#     print(f"{peleador1} golpea a {peleador2} con {golpe1} de daño. HP de {peleador2}: {max(hp2, 0)}")
#     print(f"{peleador2} golpea a {peleador1} con {golpe2} de daño. HP de {peleador1}: {max(hp1, 0)}")
#     turno += 1
# if hp1 > 0:
#     print(f"\n¡{peleador1} gana la pelea!")
# else:    print(f"\n¡{peleador2} gana la pelea!")


# crea un numero random entre 1 y 100, pide al usuario que adivine el numero, si el usuario pone un numero mayor al generado, debe decir "te pasaste ", en caso contrario, debe decir " el numero a adivinar es mayor", solo hay 5 posibilidades para adivinar el numero, si el usuario no adivina en esos 5 intentos, pierde y se muestra el numero generado al final.
numero_secreto = random.randint(1, 100)
intentos = 5
print("¡Bienvenido al juego de adivinar el número!")
print(f"Tienes {intentos} intentos para adivinar el número entre 1 y 100.")
for intento in range(1, intentos + 1):
    adivinanza = int(input(f"Intento {intento}: Ingresa tu número: "))
    if adivinanza > numero_secreto:
        print("Te pasaste.")
    elif adivinanza < numero_secreto:
        print("El número a adivinar es mayor.")
    else:
        print(f"¡Felicidades! Has adivinado el número en {intento} intentos.")
        break
else:    print(f"Lo siento, has perdido. El número secreto era {numero_secreto}.")
