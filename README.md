# GonzaloEtchechury-ProyectoFinal

![Static Badge](https://img.shields.io/badge/Build-En_progreso-red?style=flat&logo=Django)

<h4 align="center">
:construction: Proyecto en construcción :construction:
</h4>

_Este proyecto trata de emular una web de agente de ventas de pasajes aéreos, donde se podrá encontrar una página de inicio o bienvenida, una página donde se pueden ver los vuelos registrados o, en su defecto, crear uno, ingresando información en campos de Número de vuelo, Aerolínea, Fabricante y Modelo del avión, Fecha del vuelo, Imagen o foto del avión.

También un menú donde se ocupa la lista de pasajeros o clientes, donde se puede registrar nombre, apellido, fecha de nacimiento, documento y ciudad.

A su vez, tiene una parte de gestión de usuarios, donde se pueden registrar, iniciar sesión, editar los datos del usuario, colocar avatar, y finalmente una bandeja de mensajería donde interactuar con otros usuarios._


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

_Qué cosas necesitas para instalar el software y cómo instalarlas_



-Python [link de descarga](https://www.python.org/downloads/)
-Visual Studio Code [link de descarga](https://code.visualstudio.com/)
* [Video de Instalación de Python y VSC](https://www.youtube.com/watch?v=6npp93ZIQgM&ab_channel=v%C3%ADctorRomero)
-Git [link de descarga](https://git-scm.com/) 
* [Diapositivas de cómo instalar git](https://docs.google.com/presentation/d/12ov-P60D98VumjZO23Y_TMDLlX9JHUFp1amG3YJyTqI/edit?usp=drive_link)
-Navegador Web, a elección: Edge, Chrome, Firefox (Recomendado), Brave, Safari, Etc


### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutándose_

_Clonar Repositorio_

1. Ve al escritorio de tu computadora.
Crea una nueva carpeta. Puedes hacerlo haciendo clic derecho en el escritorio, seleccionando "Nuevo" y luego "Carpeta". Nombra la carpeta, por ejemplo, ProyectoDjango.

2. Adentro de la carpeta haz clic derecho.
Selecciona "Abrir con Code" o "Open with Code" del menú contextual. Esto abrirá Visual Studio Code con la carpeta seleccionada como el espacio de trabajo.

3. Abrir una terminal en Visual Studio Code
En Visual Studio Code, abre una nueva terminal bash. Puedes hacerlo desde el menú superior seleccionando Terminal > New Terminal o usando el atajo `Ctrl + ` `.

4. Clonar el repositorio
En la terminal bash, clona el repositorio en la carpeta actual usando el siguiente comando:
```
git clone https://github.com/gonzaloe281/GonzaloEtchechury-ProyectoFinal.git .
```
Nota: El "." al final del comando asegura que el contenido del repositorio se clone directamente en la carpeta actual sin crear una subcarpeta adicional.

5. Crea un entorno virtual para el proyecto
```
python -m venv env
```
"env" es el nombre del entorno virtual, puede ser cualquiera.

6. Activa el entorno virtual
```
.env\Scripts\activate
```

7. Instalar dependencias en el archivo requirements.txt
```
pip install -r requirements.txt
```

8. Realiza las migraciones de la base de datos
```
python manage.py migrate
```

9. Crea un superusuario (opcional, pero recomendado para acceder al panel de administración de Django)
```
python manage.py createsuperuser
```
Sigue las instrucciones para crear un superusuario.

10. Inicia el servidor de desarrollo de Django
```
python manage.py runserver
```
En la terminal va a aparecer el mensaje que confirma que se levantó el servidor y va a estar incluida la URL: http://127.0.0.1:8000/ mismo en la terminal apretando Ctrl + click izquierdo, abre tu navegador en esa dirección.

Con estos pasos, deberías tener tu proyecto Django clonado, configurado y en funcionamiento en tu entorno local utilizando Visual Studio Code y la terminal bash, empezando desde crear una carpeta en el escritorio. Si tienes algún problema o necesitas más detalles sobre algún paso, no dudes en decírmelo.


## Construido con 🛠️


* [Django](https://www.djangoproject.com/download/) - El framework web usado
* [HTML](https://developer.mozilla.org/es/docs/Web/HTML) - Lenguaje de etiquetas de hipertexto
* [CSS](https://developer.mozilla.org/es/docs/Web/CSS) - Hojas de Estilo en Cascada



## Autores ✒️

* **Gonzalo Etchechury** - *Trabajo Total* - [Gonzaloe281](https://github.com/gonzaloe281)
 
## Nota Final 💬

* Luego de dar muchas vueltas de cómo desarrollar el proyecto final, decidí que lo mejor en mi caso era acomodar y seguir desarrollando la tercera entrega, en lo que es código y armado, por la parte de HTML y CSS agregué mis conocimientos, ya que me sirven para aplicar lo aprendido en otros cursos, y de lo que es Python y Django, obviamente aplicar lo aprendido en las clases en vivo de CODERHOUSE y diapositivas, también en algunos puntos tuve que despejar dudas buscando en la web cómo aplicar "X" cosa en el proyecto para que funcione correctamente.

* Fue mucho esfuerzo y horas invertidas para hacerlo lo más completo posible.

* Gracias ☕🧉