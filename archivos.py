from cryptography.fernet import Fernet
from pathlib import Path


def leerArchivo(archivo):
	stream = open(archivo,"rt")#r= read, t= text
	print(stream.read())

def escribirArchivo(linea, archivo):
	with open(archivo, "a") as file: #a = append, para agregar lineas
		file.write("\n"+linea)

def generar_clave():
	archivo = r'key.key'
	objetoArchivo = Path(archivo) #determinar si la clave existe 
	if not objetoArchivo.is_file(): #si la clave no existe
		clave = Fernet.generate_key() #generamos la llave
		
		with open('key.key',"wb") as key_file: #(w=write b=binary) = archivo de escritura en modo binario  
			key_file.write(clave) #agregamos la llave creada 

def cargar_clave():
	return open("key.key", "rb").read() #(r=read b=binary) =lecura en modo binario 


def encriptar(archivo, clave):
	f = Fernet(clave)
	with open(archivo, "rb") as file:
		file_data = file.read()

	datos_encriptados = f.encrypt(file_data) #se encriptan los archivos dentro del documento que se paso a la variable file_data
	
	with open(archivo,"wb") as file:
		file.write(datos_encriptados)

def desencriptar(archivo, clave):
	f = Fernet(clave)
	with open(archivo, "rb") as file:
		datos_encriptados = file.read()
	
	datos_desencriptados = f.decrypt(datos_encriptados) #decrypt es para desencriptar los datos del archivo que contiene la variable de d_e
	with open(archivo, "wb") as file:
		file.write(datos_desencriptados)
