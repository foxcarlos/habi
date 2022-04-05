import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

from controllers.inmuebles import ControllersInmueble

_logger = logging.getLogger(__name__)


class Server(BaseHTTPRequestHandler):
    def _config_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._config_headers()

    def do_GET(self):
        """GET Methods."""

        self._config_headers()
        if not self.headers['content-length']:
            self.wfile.write(json.dumps({'response': 'Consulta no puede estar vacia'}).encode('utf-8'))
            return False

        length = int(self.headers['content-length'])
        body_json_recived = json.loads(self.rfile.read(length))
        path = self.path

        response = ControllersInmueble(body_json_recived, path)
        self.wfile.write(json.dumps({'response': response.values, 'received': 'ok'}).encode('utf-8'))

    def do_POST(self):
        """POST Methods."""

        if self.headers.get_content_type() != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        length = int(self.headers['content-length'])
        message = json.loads(self.rfile.read(length))

        message['received'] = 'ok'

        self._config_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=Server, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    _logger.info('Starting httpd on port %d', port)
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
