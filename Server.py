from http.server import HTTPServer, SimpleHTTPRequestHandler

# Definiere den Port, auf dem der Server laufen soll
port = 8000

# Erstelle eine Klasse, die SimpleHTTPRequestHandler erweitert, um die Dateien zu servieren
class CustomHandler(SimpleHTTPRequestHandler):
    # Überschreibe die Methode do_GET, um die index.html zu servieren
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # Weise den Pfad der index.html zu
        return SimpleHTTPRequestHandler.do_GET(self)

# Erstelle den Server
server_address = ('', port)  # Der Server läuft auf allen IP-Adressen des Hosts
httpd = HTTPServer(server_address, CustomHandler)

# Starte den Server
print(f"Server läuft auf Port {port}")
httpd.serve_forever()
