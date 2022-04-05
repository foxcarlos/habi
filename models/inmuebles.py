import logging

from mysql.connector import Error, connect

_logger = logging.getLogger(__name__)

# cnx = mysql.connector.connect(host="", port=3309, user='', password='')


class DBApi:
    host = "3.130.126.210"
    port = 3309
    user = "pruebas"
    password = "VGbt3Day5R"

    def connect(self):
        """Connect Method."""
        self.connection = False

        try:
            self.connection = connect(
                host=self.host, port=self.port, user=self.user, password=self.password, database="habi_db"
            )
        except Error as error:
            _logger.error(error)

        return self.connection

    def exec_query(self, sql_query):
        rows = []
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
        except Error as error:
            _logger.error(error)

        return rows


class ModelsInmueble:
    def search_by_status(self, body_json_recived):
        """Serach depto by status.
        params recived: {"status_search": [3, 2]}"""

        get_status_ids = ", ".join(map(str, body_json_recived.get('status_search')))
        status_ids = get_status_ids or '3, 4, 5'  # POr defecto si no se selecciona ninguna busqueda devuelve esos 3

        sql_query = f"""select sh.id, sh.property_id, p.address, p.city, p.price, p.description, sh.status_id,
        s.name from status_history as sh
        left join `status` as s on sh.status_id = s.id
        left join property as p on sh.property_id = p.id
        where s.id in ({status_ids})
        """
        db = DBApi()
        db.connect()
        result = db.exec_query(sql_query)
        db.connection.close()

        values = {"inmuebles por status": result}
        return values

    def filter_by(self, body_json_recived):
        """Filter inmuebles by: Construnction Years, City, Province."""

        # Los usuarios pueden filtrar estos inmuebles por:
        # Año de construcción,
        # Ciudad,
        # Estado.
        # Los usuarios pueden aplicar varios filtros en la misma consulta.
        # Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
        # Estado, Precio de venta y Descripción.
        values = {"inmuebles por A;o, ciudad, Estado": ['cuatro', 'cinco', 'seis']}
        return values
