import http.server
import socketserver
import webbrowser
import os

# Configuración del servidor
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

# Cambiar al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Iniciar el servidor
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor corriendo en http://localhost:{PORT}")
    print("Presiona Ctrl+C para detener el servidor")
    
    # Abrir el navegador automáticamente
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Mantener el servidor corriendo
    httpd.serve_forever()
