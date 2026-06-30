# crear una funcion donde le pasa la lista como parametro 
# esta funcion debe mostrar todos los datos del diccionario

# def mostrar_datos(lista):
#     for diccionario in lista:
#         for clave, valor in diccionario.items():
#             print(f"{clave}: {valor}")
#         print()


# datos = [
#     {"nombre": "Ana", "edad": 28, "ciudad": "Lima"},
#     {"nombre": "Luis", "edad": 35, "ciudad": "Cusco"},
#     {"nombre": "Marta", "edad": 22, "ciudad": "Arequipa"}
# ]

# mostrar_datos(datos)


autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
    'A007' : ['Chevrolet', 'cruze',1958,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','12-10-2025'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
    'A007' : ['24-03-2024','24-09-2025'],
}


def mostrar_datos(lista):
    for codigo, valores in lista.items():
        print ( f"{codigo} .- {valores}")

mostrar_datos(autos)

def vendidos(lista):
    for codigo, valores in lista.items():
        if operaciones[codigo][1] != "Pendiente":
            print(f"{codigo} .- {valores}")
print("-"*50)
vendidos(autos)


# def agregar_vehiculo(autos, operaciones, codigo, marca, modelo, anio, puertas, fecha_inicio, fecha_fin="Pendiente"):
#     if codigo in autos:
#         print(f"El código {codigo} ya existe.")
#         return
#     autos[codigo] = [marca, modelo, anio, puertas]
#     operaciones[codigo] = [fecha_inicio, fecha_fin]
#     print(f"Vehículo {codigo} agregado.")

# print("-"*50)
# agregar_vehiculo(autos, operaciones, 'A008', 'Nissan', 'Versa', 2023, 4, '01-06-2025')
# print("-"*50)
# mostrar_datos(autos)


def crearveh(dic):
    marca=input("Ingrese la marca: ")
    modelo=input("Ingrese el modelo: ")
    anio=int(input("Ingrese el año: "))
    ranking=int(input("Ingrese el ranking: "))
    codigo=input("Ingrese el codigo: ")
    dic[codigo]=[marca,modelo,anio,ranking]

 