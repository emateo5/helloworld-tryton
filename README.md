# helloworld-tryton
Helloworld Tryton example from wiki.

Para el despliegue utilizar

Puedes copiar el modulo dentro del directorio de módulos de trytond (trytond/modules).

Luego tienes que actualizar la lista de módulos con el comando:
 ./trytond -d base_de_datos -u cualquier_modulo_ya_instalado

Una vez actualizada la base de datos, puedes reiniciar el servicio trytond y deberías tener el nuevo módulo en la lista de módulos disponibles para instalar en el sistema.

Saludos Edwin


NOTA no es necesario utilizar el archivo setup.py - si deseas lo borras
