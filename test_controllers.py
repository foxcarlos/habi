#!/usr/bin/env python
import unittest

from controllers.inmuebles import ControllersInmueble
from models.inmuebles import ModelsInmueble, DBApi


class TestControllers(unittest.TestCase):
    def test_paht_empty(self):
        pnf = ControllersInmueble({}, '')
        result = pnf._not_found('')
        self.assertEqual(result, {"message": "PAGE NOT FOUND"})

    def test_search_inmueble_name(self):
        body_json_recived = {"status_search": ["vendido"]}
        sbs = ControllersInmueble._search_by_status_name(self, body_json_recived)
        self.assertTrue(sbs)

    def test_search_inmueble(self):
        body_json_recived = {"status_search": [3, 4, 5]}
        sbs = ControllersInmueble._search_by_status(self, body_json_recived)
        self.assertTrue(sbs)

    def test_filter_inmueble_with_json(self):
        body_json_recived = {"year": "2000", "city": "bogota", "status_name": "pre_venta"}
        response = ControllersInmueble(body_json_recived, '/filter/')
        sbs = response._filter_by(body_json_recived)
        self.assertTrue(sbs)

    def test_filter_inmueble_without_json(self):
        body_json_recived = {}
        response = ControllersInmueble(body_json_recived, '/filter/')
        sbs = response._filter_by(body_json_recived)
        self.assertTrue(sbs)


class TestModelsInmuebleDBApi(unittest.TestCase):
    def test_connect_ok(self):
        db = DBApi()
        connect = db.connect()
        self.assertTrue(connect)

    def test_connect_fail(self):
        db = DBApi()
        db.host = '0.0.0.0'
        connect = db.connect()
        self.assertFalse(connect)

    def test_query_ok(self):
        db = DBApi()
        db.connect()
        result = db.exec_query("SELECT CURDATE()")
        self.assertTrue(result)


class TestModelsInmueble(unittest.TestCase):
    def test_parse_search_data_empty(self):
        model_inmueble = ModelsInmueble()
        result = model_inmueble.parse_search_data("")
        self.assertEqual(result, [])

    def test_parse_search_data_ok(self):
        data = [(3, 1, 'calle 23 #45-67', 'bogota', 120000000,
                'Hermoso apartamento en el centro de la ciudad', 3, 'pre_venta')]
        model_inmueble = ModelsInmueble()
        result = model_inmueble.parse_search_data(data)
        self.assertTrue(result)

    def test_search_by_satus_name_ok(self):
        json = {"status_search": ["pre_venta", "vendido"]}
        model_inmueble = ModelsInmueble()
        result = model_inmueble.search_by_status_name(json)
        self.assertTrue(result)

    def test_search_by_satus_name_not_found(self):
        json = {"status_search": ["otro"]}
        model_inmueble = ModelsInmueble()
        result = model_inmueble.search_by_status_name(json)
        self.assertEqual(result, {'inmuebles por status': []})

    def test_filter_by_ok(self):
        json = {"year": "2000", "city": "bogota", "status_name": "pre_venta"}
        model_inmueble = ModelsInmueble()
        result = model_inmueble.filter_by(json)
        length = len(result.get('inmuebles por Anio, ciudad, status'))
        self.assertGreater(length, 0)

    def test_filter_by_not_found(self):
        json = {"year": "3000"}
        model_inmueble = ModelsInmueble()
        result = model_inmueble.filter_by(json)
        length = len(result.get('inmuebles por Anio, ciudad, status'))
        self.assertEqual(length, 0)


if __name__ == "__main__":
    unittest.main()
