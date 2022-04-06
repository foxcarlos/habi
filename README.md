# habi

Habi Api Rest python

Tecnologias a usar en el proyecto:
- API REST:
    Al no poder usar un Framework intentare crear mi propio ApiRest usando el modulo http.server
- Base de datos:
    Para MySQL se utilizara em modulo mysql.connector

Pasos a seguir para la contruccion:

1. Crear el servicio de ApiRest usando el modulo http.server,esto incluye los metodos GET y POST('En caso de ser necesario')
    - Desde consola instalar los requirements:
     - $ python3.9 --version o Superior
     - $ pip install requirements.txt

    - Para levantar el servidor ejecutar:
     - $ python server.py

2. Crear la conexion con la base de datos mysql y hacer pruebas de consulta con pytnon y con alguna app GUI.
    - Para conectarse y realizar consultas a la base de datos desde un archivo .py o desde una shell python:

     - from models.inmuebles import DBApi

      - db = DBApi()
      - db.connect()
      - result = db.exec_query("Select * FROM status")
      - print(result)
      - db.connection.close()

3. Al tener creado el servicio Apirest proceder a crear los Servicios de consulta basados en las peticiones json (No se incluira Frontend, solo las peticiones desde PostMan)
    - 3.1 Los usuarios pueden consultar los inmuebles con los estados: “pre_venta”, “en_venta” y “vendido” (los inmuebles con estados distintos nunca deben ser visibles por el usuario).
    - 3.2 Los usuarios pueden filtrar estos inmuebles por: Año de construcción, Ciudad, Estado.
    - 3.3 Los usuarios pueden aplicar varios filtros en la misma consulta.
    - 3.4 Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad, Estado, Precio de venta y Descripción.

    Para realizar pruebas desde consola hacer las siguientes peticiones:
    - Para Buscar inmuebles por el id del estado:
      - $ curl -X GET -d '{"status_search": [3]}' -H "Content-Type: application/json" http://localhost:8000/search/inmuebles/

    - Buscar por varios ID de estados a la vez:
      - $ curl -X GET -d '{"status_search": [3, 4, 5]}' -H "Content-Type: application/json" http://localhost:8000/search/inmuebles/

    - Buscar por nombres de estados (un solo estado o varios a la vez)
      - $ curl -X GET -d '{"status_search": ["pre_venta", "vendido"]}' -H "Content-Type: application/json" http://localhost:8000/search/inmuebles/name/
      - $ curl -X GET -d '{"status_search": ["en_venta"]}' -H "Content-Type: application/json" http://localhost:8000/search/inmuebles/name/

    - Para filtrar inmuebles por diferentes campos:
      - $ curl -X GET -d '{"year": "2000"}' -H "Content-Type: application/json" http://localhost:8000/filter/
      - $ curl -X GET -d '{"city": "bogota"}' -H "Content-Type: application/json" http://localhost:8000/filter/
      - $ curl -X GET -d '{"status_name": "pre_venta"}' -H "Content-Type: application/json" http://localhost:8000/filter/

    - Por varios campos a la vez:
      - $ curl -X GET -d '{"year": "2000", "city": "bogota", "status_name": "pre_venta"}' -H "Content-Type: application/json" http://localhost:8000/filter/

4. Servicio de “Me gusta”
    - 4.1 Hacer el analisis de entidad relacion para el servicio Me Gusta.
    - Una Tabla llamada historico_me_gusta
        Campos:
        - id
        - property_id
        - user_id
        - date
        - me_gusta default=true
        
![image](https://github.com/foxcarlos/habi/blob/main/relacion.png)


5. Crear los Test Case
    - para ejecutar los test ejecutar desde consola:
      - $ python test_controllers.py


6. DESAFIOS:
  - Siempre he trabajado con framework para realizar estas acciones
  - Tengo bastante tiempo que no trabajo con MYSQL
