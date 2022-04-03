# habi

Habi Api Rest python

Tecnologias a usar en el proyecto:
- API REST:
    Al no poder usar un Framework intentare crear mi propio ApiRest usando el modulo http.server
- Base de datos:
    Para MySQL se utilizara em modulo mysql.connector

Pasos a seguir para la contruccion:

1.- Crear el servicio de ApiRest usando el modulo http.server,esto incluye los metodos GET y POST('En caso de ser necesario')

2.- Crear la conexion con la base de datos mysql y hacer pruebas de consulta con pytnon y con alguna app GUI.
    2.1 

3.- Al tener creado el servicio Apirest proceder a crear los Servicios de consulta basados en las peticiones json (No se incluira Frontend, solo las peticiones desde PostMan)
    3.1 Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y “vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).
    3.2 Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.
    3.3 Los usuarios pueden aplicar varios filtros en la misma consulta.
    3.4 Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad, Estado, Precio de venta y Descripción.

4.- Servicio de “Me gusta”
    4.1 Hacer el analisis de entidad relacion para el servicio Me Gusta.

5.- Crear los Test Case

# DESAFIOS:
    Siempre he trabajado con framework para realizar estas acciones
    Tengo bastante tiempo que no trabajo con MYSQL
