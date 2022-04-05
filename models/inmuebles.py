import logging
import os
from configparser import ConfigParser

from mysql.connector import Error, connect

_logger = logging.getLogger(__name__)


current_path = os.path.dirname(os.path.abspath(__file__))
path_conf = os.path.dirname(current_path)
file = os.path.join(path_conf, 'app.conf')

parser = ConfigParser()
parser.read(file)


class DBApi:

    host = parser.get('MYSQL', 'host')  # "3.130.126.210"
    port = parser.get('MYSQL', 'port')  # 3309
    user = parser.get('MYSQL', 'user')  # "pruebas"
    password = parser.get('MYSQL', 'password')  # "VGbt3Day5R"

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
    def parse_search_data(self, result):
        rows = []
        for _id, property_id, address, city, price, description, status_id, status_name in result:
            vals = {
                'id': _id,
                'property_id': property_id,
                'address': address,
                'city': city,
                'price': price,
                'description': description,
                'status_id': status_id,
                'status_name': status_name,
            }
            rows.append(vals)
        return rows

    def search_by_status_name(self, body_json_recived):
        """Search depto by status.
        Params recived:
        Method GET:
        Body Raw: {"status_search": ['pre_venta', 'en_venta', 'vendido']} # Pudiera ser un POST
        Content-Type: JSON"""

        sentence = ''
        get_status_names = body_json_recived.get('status_search') or []
        for value in get_status_names:
            sentence += f"'{value}',"

        sentence = sentence[:-1] if sentence.endswith(',') else sentence
        status_names = sentence or '"pre_venta", "en_venta", "vendido"'
        # Por defecto si no se selecciona ninguna busqueda devuelve esos 3

        sql_query = f"""select sh.id, sh.property_id, p.address, p.city, p.price, p.description, sh.status_id,
        s.name from status_history as sh
        left join `status` as s on sh.status_id = s.id
        left join property as p on sh.property_id = p.id
        where s.name in ({status_names})
        """
        rows = []
        db = DBApi()
        db.connect()
        result = db.exec_query(sql_query)
        db.connection.close()
        rows = self.parse_search_data(result)

        values = {"inmuebles por status": rows}
        return values

    def search_by_status(self, body_json_recived):
        """Search depto by status.
        Params recived:
        Method GET:
        Body Raw: {"status_search": [3, 2]} # Pudiera ser un POST
        Content-Type: JSON"""

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

        rows = []
        rows = self.parse_search_data(result)
        values = {"inmuebles por status": rows}
        return values

    def filter_by(self, body_json_recived):
        """Filter inmuebles by: Construnction Years, City, status."""

        sentence = ''
        for key, value in body_json_recived.items():
            if key == 'status_name':
                sentence += f"status.name = '{value}' AND "
            else:
                sentence += f"{key} = '{value}' AND "

        sql_query = f"""select property.id as pid, address, city, price, description, `year`,
        status_history.status_id, `status`.`name` as status_name  from property
        LEFT OUTER JOIN status_history  ON property.id = status_history.property_id
        LEFT OUTER Join `status` on status_history.status_id = `status`.`id`
        WHERE status_history.status_id in (3, 4, 5) AND {sentence}"""

        where_sentence = sql_query[:-4] if sql_query.endswith('AND ') else sql_query

        db = DBApi()
        db.connect()
        result = db.exec_query(where_sentence.strip())
        db.connection.close()

        rows = []
        for _id, address, city, price, description, year, id_status, status_name in result:
            vals = {
                'id': _id,
                'address': address,
                'city': city,
                'price': price,
                'description': description,
                'year': year,
                'id_status': id_status,
                'status_name': status_name,
            }
            rows.append(vals)

        values = {"inmuebles por Anio, ciudad, status": rows}
        return values
