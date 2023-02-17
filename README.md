# Crebiks
*Modelado de cubos rubiks cuadrados y rectangulares*

# ¿Como usar este proyecto?
* 1- tener instalado docker(si no quieres usar docker debes omitir el paso 7)
* 2- Clonar repo
* 3- Situarse en la raiz del proyecto
* 4- Crear archivo ".env" con este contenido "SECRET_KEY = '-----your secret key-----'":
  
  ![image](https://user-images.githubusercontent.com/83993271/219707045-95b78f7a-aba1-4084-a483-f809bee99f47.png)

* 5- Generar secret key para Django(la mia la genere con la pagina https://djecrety.ir/ y le reemplace algunos caracteres) y reemplazarla en el .env que creamos
  
  ![image](https://user-images.githubusercontent.com/83993271/219708376-d7919307-0d48-406c-8e5b-c1a97fd3552b.png)

* 6- La estructura del proyecto resulta así:

  ![image](https://user-images.githubusercontent.com/83993271/219709302-4d6fdadd-d783-44db-a539-e2ac7f9428c7.png)

* 7- En la raiz del proyecto ejecutar estos comandos por consola(debes tener docker):
  * docker-compose build
  * docker-compose up
  
* 8- **Ignorar este paso si usas docker**. Debes instalar Python 3 o superior y instalar con pip install Django 4.1.4 y python-decuple, para levantar el servidor ejecutar camando "python manage.py runserver" en la raiz del proyecto desde consola de comandos.
