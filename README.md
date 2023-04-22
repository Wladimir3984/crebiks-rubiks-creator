# Crebiks, Crear modelos de cubos rubiks nunca fue tan facil :D
*Modelado de cubos rubiks cuadrados y rectangulares*

## Buscando la formula para descomponer un cubo rubik 
**sin importar la orientación del cubo a la hora de designar alto x ancho x profundidad**

![borrador formula](https://user-images.githubusercontent.com/83993271/221079805-198cbca4-af83-40e5-a8d5-6241385b6112.jpeg)
*¿será correcta esta descomposición del cubo de rubik? ¡compruebalo tu mismo usando esta aplicación web!*

## ¿Como usar este proyecto?
* 1- tener instalado docker(si no quieres usar docker debes omitir el paso 7)
* 2- Clonar repo
* 3- Situarse en la raiz del proyecto
* 4- Crear archivo ".env" con este contenido "SECRET_KEY = '-----your secret key-----'":
  
  ![image](https://user-images.githubusercontent.com/83993271/219707045-95b78f7a-aba1-4084-a483-f809bee99f47.png)

* 5- Generar secret key para Django(la mia la genere con la pagina https://djecrety.ir/ y le reemplace algunos caracteres) y reemplazarla en el .env que creamos
  
  ![image](https://user-images.githubusercontent.com/83993271/219708376-d7919307-0d48-406c-8e5b-c1a97fd3552b.png)

* 6- La estructura del proyecto resulta así:

  ![image](https://user-images.githubusercontent.com/83993271/219709302-4d6fdadd-d783-44db-a539-e2ac7f9428c7.png)

* 7- **En caso de usar docker**, en la raiz del proyecto ejecutar los siguientes comandos por consola:
  * docker-compose build
  * docker-compose up
  
* 8- **En caso de NO usar docker**, debes instalar Python 3 o superior y ejecutar con pip las dependencias del proyecto documentadas en el archivo requirements.txt, para levantar el servidor ejecutar comando "python manage.py runserver" en la raiz del proyecto desde consola de comandos.
