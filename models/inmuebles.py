import logging
from getpass import getpass

from mysql.connector import Error, connect

_logger = logging.getLogger(__name__)

# cnx = mysql.connector.connect(host="", port=3309, user='', password='')


class DBConnect:
    host = "3.130.126.210"
    port = 3309
    user = ""
    password = ""

    def my_connect(self):
        """Connect Method."""
        connection = False

        try:
            connection = connect(
                host=self.host,
                port=self.port,
                user=input("Ingrese el usuario"),
                password=getpass("Ingrese el password"),
            )
        except Error as error:
            _logger.error(error)

        return connection


class ModelsInmueble:
    def search_by_state(self, body_json_recived):
        """Serach depto by state."""

        # "pre_venta”,
        # “en_venta”
        # “vendido”
        # (los inmuebles con estados distintos nunca deben ser visibles por el usuario)
        # Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
        # Estado, Precio de venta y Descripción.

        values = {"inmuebles por estado": ['uno', 'dos', 'tres']}
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
