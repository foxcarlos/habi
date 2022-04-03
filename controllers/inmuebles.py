import logging

_logger = logging.getLogger(__name__)


class ControllersInmueble:
    values = str

    def __init__(self, body_json_recived, path):
        _logger.info(body_json_recived, path)

        if path == '/search/inmuebles/':
            self._search_by_state(body_json_recived)

        elif path == '/filter/':
            self._filter_by(body_json_recived)

        else:
            self._not_found(path)

    def _not_found(self, path):
        self.values = {"message": "PAGE NOT FOUND"}
        return self.values

    def _search_by_state(self, body_json_recived):
        """Serach depto by state."""

        # "pre_venta”,
        # “en_venta”
        # “vendido”
        # (los inmuebles con estados distintos nunca deben ser visibles por el usuario)
        # Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
        # Estado, Precio de venta y Descripción.

        self.values = {"inmuebles por estado": ['uno', 'dos', 'tres']}
        return self.values

    def _filter_by(self, body_json_recived):
        """Filter inmuebles by: Construnction Years, City, Province."""

        # Los usuarios pueden filtrar estos inmuebles por:
        # Año de construcción,
        # Ciudad,
        # Estado.
        # Los usuarios pueden aplicar varios filtros en la misma consulta.
        # Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
        # Estado, Precio de venta y Descripción.
        self.values = {"inmuebles por A;o, ciudad, Estado": ['cuatro', 'cinco', 'seis']}
        return self.values
