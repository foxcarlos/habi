#!/usr/bin/env python
import unittest

from controllers.inmuebles import ControllersInmueble


class TestControllers(unittest.TestCase):
    def test_paht_empty(self):
        pnf = ControllersInmueble({}, '')
        result = pnf._not_found('')
        self.assertEqual(result, {"message": "PAGE NOT FOUND"})

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


if __name__ == "__main__":
    unittest.main()
