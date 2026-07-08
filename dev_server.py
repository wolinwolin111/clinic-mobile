import http.server
import urllib.request
import socketserver
import os

API_TARGET = 'http://66.154.101.204'
PORT = 3000
WWW_DIR = os.path.join(os.path.dirname(__file__), 'www')

os.chdir(WWW_DIR)
print(f'Serving from: {WWW_DIR}')

class ProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if path.startswith('/api/'):
            target = API_TARGET + path
            try:
                resp = urllib.request.urlopen(target, timeout=10)
                self.send_response(resp.status)
                self.send_header('Content-Type', resp.headers.get('Content-Type', 'application/json'))
                self.end_headers()
                self.wfile.write(resp.read())
            except Exception as e:
                self.send_response(502)
                self.end_headers()
                self.wfile.write(str(e).encode())
            return

        super().do_GET()

    def do_POST(self):
        if self.path.startswith('/api/'):
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length) if length else b''
            target = API_TARGET + self.path
            try:
                req = urllib.request.Request(target, data=body, headers={'Content-Type': 'application/json'})
                req.method = 'POST'
                resp = urllib.request.urlopen(req, timeout=10)
                self.send_response(resp.status)
                self.send_header('Content-Type', resp.headers.get('Content-Type', 'application/json'))
                self.end_headers()
                self.wfile.write(resp.read())
            except Exception as e:
                self.send_response(502)
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            super().do_GET()

    def do_PUT(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length else b''
        target = API_TARGET + self.path
        try:
            req = urllib.request.Request(target, data=body, headers={'Content-Type': 'application/json'})
            req.method = 'PUT'
            resp = urllib.request.urlopen(req, timeout=10)
            self.send_response(resp.status)
            self.send_header('Content-Type', resp.headers.get('Content-Type', 'application/json'))
            self.end_headers()
            self.wfile.write(resp.read())
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def do_DELETE(self):
        target = API_TARGET + self.path
        try:
            req = urllib.request.Request(target, method='DELETE')
            resp = urllib.request.urlopen(req, timeout=10)
            self.send_response(resp.status)
            self.send_header('Content-Type', resp.headers.get('Content-Type', 'application/json'))
            self.end_headers()
            self.wfile.write(resp.read())
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(str(e).encode())

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Max-Age', '86400')
        self.end_headers()

Handler = ProxyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f'http://localhost:{PORT} (API proxied to {API_TARGET})')
    print(f'Root / -> 302 -> /test.html')
    httpd.serve_forever()
