import http.server

n = 0

def obtenirDocument(path):
    global n
    n += 1
    print(n, path)
    return template.replace('NUM', str(n)).replace('PATH', path)

template = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>PATH</title>
  </head>
  <body>
    <h1>requete #NUM: path = PATH</h1>
  </body>
</html>"""

class ServeurWeb(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        doc = obtenirDocument(self.path)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(doc.encode('utf-8'))

    def log_message(self, format, *args):
        pass

http.server.HTTPServer(('localhost', 8000), ServeurWeb).serve_forever()
