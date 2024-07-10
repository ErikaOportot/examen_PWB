Bienvenido a la inicialización del repositorio de Erika Oportot

1.-Para comenzar, crea una carpeta en escritorio o documentos, luego al ingresar, selecciona 
"Archivo" -->Windows PowerShell -> abrir como administrador.

2.-Ahora debemos revisar las versiones de Python y PIP para asegurarnos de tener las mismas 
y evitar errores ejecutando "python --version" y "pip --version" (si deseas actualizar la versión de PIP ejectuta "python -m pip install --upgrade pip")

3.- Una vez verificado, ejecutamos el comando "git clone https://github.com/ErikaOportot/examen_erikaOportot.git" 
comenzamos creando nuestro ambiente virtual para luego instalar las dependencias. Para ello, 
ejecutamos "python -m venv myvenv" para recrear el ambiente virtual.

4.- Activamos el ambiente siguiendo el comando "cd myvenv" + tab luego "cd Scripts" +tab y finalmente
"activate"

5.- retrocedemos con el comando "cd .." hasta volver a la carpeta "examen Web", y ejecutamos el comando "pip install -r requirements.txt"

6.- finalmente en "cd Biblioteca" ejecutamos "python manage.py runserver"

IMPORTANTE: En caso que arroje error de permisos de ejecucion de scripts, digitar el comando "Set-ExecutionPolicy Unrestricted"
