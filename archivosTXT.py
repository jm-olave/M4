# lectura del archivo
# try:
#     archivo = open("archivo.txt","r")
#     contenido = archivo.read()
# except FileNotFoundError:
#     print("no encontro el archivo")
# else:   
#     print(contenido)
# finally:
#     archivo.close()
#     print(archivo.closed)

# escritura del archivo
# archivo = open("archivo.txt","r+")
# archivo.seek(0,2)
# print(archivo.tell())
# archivo.write("Nueva linea")

# archivo.close()

# crear un archivo
# archivo2 = open("archivo2.txt","w")
# archivo2.write("Linea 1\n")
# archivo2.seek(0,2)
# archivo2.write("Linea 2\n")
# archivo2.close()

# content manager
# escritura
# with open("archivo.txt","r") as documento:
#     lineas = documento.readlines()
#     print(lineas)
#     for linea in lineas:
#         print(linea, end="*")

# lectura
# with open("archivo2.txt","w") as documento:
#     documento.write("Nueva Linea")

# with open("archivo.txt","r") as documento:
#     lineas = documento.read(10)
#     while len(lineas) > 0:
#         print(lineas, end="*")
#         lineas = documento.read(10)


# realizar copia de un archivo
with open("archivo.txt","r") as document:
    with open("archivo_copy.txt", "w") as copia:
        for linea in document:
            copia.write(linea)