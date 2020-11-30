from Crypto.Cipher import DES
# Como usamos DES, los bloques son de 8 caracteres.
# Rellenamos con espacios (que habra que eliminar al descifrar).
usuario =  input("ingresa tu nombre (8caracteres contando el espacio)\t")
password = input("ingresa tu contraseña(8caracteres contando el espacio)\t")
# creamos el cifrador con DES
cipher = DES.new('12345678')
# ciframos usuario y password
c_usuario = cipher.encrypt(usuario)
c_password = cipher.encrypt(password)
# enviamos credenciales (a la pantalla en este caso)
print ("El cliente envia:")
print ("Usuario: " + str(c_usuario))
print ("Password: " + str(c_password))

#------------------------------------------------------------------
# a partir de aqui simulamos el servidor donde llegan los mensajes
# cifrados.
# desciframos mensajes y quitamos espacios con strip()
cipher = DES.new('12345678')
d_usuario = cipher.decrypt(c_usuario).strip()
d_password = cipher.decrypt(c_password).strip()
print ("El servidor descifra:")
print ("Usuario: " + str(d_usuario))
print ("Password: " + str(d_password))

