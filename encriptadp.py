import archivos #documento que contiene nuestros metodos 


opcion = 0

archivos.generar_clave()
clave = archivos.cargar_clave()

archivo = "hola"

while opcion != 5:

	print("\nSelecciona una opcion")
	print("\n1. Leer archivo\n2. Agregar texto al archivo\n3. Encriptar\n4. Desencriptar\n5. Salir")
	opcion = int(input("Ingresa una opcion:\t"))
	if opcion == 1:
		print("El contenido del archivo es: \n")
		archivos.leerArchivo(archivo) #lo que esta dentro del parentesis es el nombre de la variable que contiene nuestro archivo 
	elif opcion == 2:
		linea = input("Ingresa el texto a agrdgar en el txt\t")
		archivos.escribirArchivo(linea, archivo) #lo que esta dentro del parentesis es lavariable que contiene lo que ingresaremos al txt
	elif opcion == 3:
		archivos.encriptar(archivo, clave)
		print("Archivo encriptado correctament")	
	elif opcion == 4:
		archivos.desencriptar(archivo, clave)
		print("los datos han sido desencriptados")
	else:
		print("OPCION SELECIONADA INCORRECTA")
