import logging

# import json

_logger = logging.getLogger(__name__)


class ControllersInmueble:
    def __init__(self, body_json_recived, path):
        _logger.info(body_json_recived, path)
        if path == '/search/inmuebles/':
            _logger.info('Buscar inmuebles')

    def _search_by_state(self, **kwargs):
        """Serach depto by state."""

        # "pre_venta”,
        # “en_venta”
        # “vendido”
        # (los inmuebles con estados distintos nunca deben ser visibles por el usuario)
        # Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
        # Estado, Precio de venta y Descripción.

    def _filter_by(self, **kwargs):
        """Filter inmuebles by: Construnction Years, City, Province."""

        # Los usuarios pueden filtrar estos inmuebles por:
        # Año de construcción,
        # Ciudad,
        # Estado.
        # Los usuarios pueden aplicar varios filtros en la misma consulta.
        # Los usuarios pueden ver la siguiente información del inmueble: Dirección, Ciudad,
        # Estado, Precio de venta y Descripción.
