
mi_diccionario ={
    "nombre": "Anthony",
    "edad": 26,
    "ciudad" : "Guayaquil"
}

# print(mi_diccionario)
# print(type(mi_diccionario))

print(mi_diccionario["nombre"]) #Anthony

nombre = mi_diccionario["nombre"]
print(nombre) #Anthony

print(mi_diccionario["edad"])

edad = mi_diccionario["edad"]
print(edad)

print(mi_diccionario["ciudad"])
ciudad= mi_diccionario["ciudad"]
print(ciudad)


mi_diccionario["profesion"]="Ingeniero"
print(mi_diccionario["profesion"])

for clave in mi_diccionario:
    print(clave)

for clave,valor in mi_diccionario.items():
    print(clave,valor)

if "nombre" in mi_diccionario:
    print("la clave 'nombre' se encuentra en el diccionaro")

if "apellido" not in mi_diccionario:
    print("La clave 'apellido' no se encuentra en el diccionario")

if "ciudad" in mi_diccionario:
    print("la clave 'ciudad' se encuentra en el diccionario")

if "profesion" not in mi_diccionario:
    print("La clave 'profesion'  se encuentra en el diccionario")

if "edad" in mi_diccionario:
    print("La clave 'edad' se encuentra en el diccionario")

if "telefono" not in mi_diccionario:
    print("La clave 'telefono' no se encuentra en el diccionario")