
Desarrollado por: Sergio Andrés Londoño Guerrero.

Esta desarrollado con la librería django 3.2.5  

Para correr la aplicación asegúrese de tener instalado python y la librería django
 -->desde el cmd o una terminal ubíquese en la carpeta del proyecto
 -->Ejecute el comando “python manage.py runserver” (esto corre un servidor interno en el equipo)
 -->Verifique el puerto que activó el comando anterior. Por defecto es 127.0.0.1:8000   
 -->Desde cualquier navegador digite la dirección del puerto anterior y ya podrá interactuar con la interfase.

Para modificar las bases de datos de los elementos 


En esta se pueden añadir, eliminar o editar los diferentes elementos que se pueden seleccionar para el viaje. 


Filosofía de solución:
Este problema de optimización se soluciona generando indicadores de eficiencia de cada uno de los objetos de la base de datos dividiendo las calorías que aporta entre su peso.
Con esto se puede realizar un ordenamiento de mayor a menor según la eficiencia de cada uno de los elementos.
Posteriormente se realizan las comparaciones para cumplir los requisitos de calorías y peso solicitadas por formulario y se imprime la lista de objetos seleccionados en pantalla.
