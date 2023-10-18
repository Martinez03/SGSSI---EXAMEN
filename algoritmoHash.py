import hashlib
import os
carpeta = "imagen"
imagenes = os.listdir(carpeta)
hashCon = "e5ed313192776744b9b93b1320b5e268"
	

for imagen in imagenes:
	ruta_archivo = os.path.join(carpeta, imagen)
	with open(ruta_archivo, "rb") as imagen:
        	hash_calculado = hashlib.md5(imagen.read()).hexdigest()
        	if hash_calculado == hashCon:
        		print(imagen)
	







