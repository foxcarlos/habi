import logging

from models.inmuebles import ModelsInmueble

_logger = logging.getLogger(__name__)


class ControllersInmueble:
    values = str

    def __init__(self, body_json_recived, path):
        _logger.info(body_json_recived, path)

        if path == '/search/inmuebles/name/':
            self._search_by_status_name(body_json_recived)

        elif path == '/search/inmuebles/':
            self._search_by_status(body_json_recived)

        elif path == '/filter/':
            self._filter_by(body_json_recived)

        else:
            self._not_found(path)

    def _not_found(self, path):
        self.values = {"message": "PAGE NOT FOUND"}
        return self.values

    def _search_by_status_name(self, body_json_recived):
        """Controllers Search depto by status name."""

        model_inmueble = ModelsInmueble()
        response = model_inmueble.search_by_status_name(body_json_recived)
        self.values = response
        return self.values

    def _search_by_status(self, body_json_recived):
        """Controllers Search depto by status."""

        model_inmueble = ModelsInmueble()
        response = model_inmueble.search_by_status(body_json_recived)
        self.values = response
        return self.values

    def _filter_by(self, body_json_recived):
        """Controllers Filter inmuebles by: Construnction Years, City, status."""

        model_inmueble = ModelsInmueble()
        response = model_inmueble.filter_by(body_json_recived)
        self.values = response
        return self.values
