# indexacion: accede a un caracter por su indice
# name="benja"
# print(name[0])
# print(len(name))
# print(name.strip())
# print(name.upper())
# print(name.lower())
# print(name.replace("b", "B"))
# print(name.split("e")) 


# pedir al usuario la clave y verificar que sea SHAZAM independientemente de su case 
clave=input("ingrese la clave: ")
if clave.upper() == "SHAZAM":
    print("clave correcta")
else:
    print("clave incorrecta")

# crear un nombre de usuario y verificar su largo este entre 4 y 10 caracteres
username=input("ingrese un nombre de usuario: ")        
if len(username) >= 4 and len(username) <= 10:
    print("nombre de usuario valido")   
else:    print("nombre de usuario invalido")


#crear un pin y que este tenga exactamente 4 digitos 
pin=input("ingrese el pin: ")
if len(pin) == 4:
    print("pin valido")
else:
    print("pin invalido")