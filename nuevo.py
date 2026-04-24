# definir 2 candidatos. Preguntar la cantidad de votantes. Luego preguntar a cada votante por quien votara mostrando las alternativas. contar los votos y mostrar resultados. Definir el ganador y considerar un empate
candidato1 = "Candidato A"
candidato2 = "Candidato B" 
votos_candidato1 = 0
votos_candidato2 = 0
cantidad_votantes = int(input("Ingrese la cantidad de votantes: "))
for i in range(cantidad_votantes):
    voto = int(input(f"Votante {i+1}, por favor ingrese su voto ({candidato1} o {candidato2}): "))
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    else:
        print("Voto inválido. Por favor, ingrese un voto válido.")
print(f"Resultados:\n{candidato1}: {votos_candidato1} votos\n{candidato2}: {votos_candidato2} votos")
if votos_candidato1 > votos_candidato2:
    print(f"El ganador es: {candidato1}")   
elif votos_candidato2 > votos_candidato1:
    print(f"El ganador es: {candidato2}")
else:    print("¡Es un empate!")