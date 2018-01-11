from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write()

    def do_POST(self):
        self._set_headers()
        # get the json length
        content_length = int(self.headers['Content-Length'])
        # get the data
        post_data = self.rfile.read(content_length)
        print(post_data)
        # write the data and response to the client
        self.wfile.write(post_data)

    def do_HEAD(self):
        self._set_headers()


def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
