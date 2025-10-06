
import http.server
import socket
import platform
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" and os.path.exists("index.html"):
            self.path = "/index.html"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def run_server():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("="*60)
    print(" PYTHON LOCAL WEB SERVER ".center(60, "="))
    print("="*60)
    print(f" Hostname : {hostname}")
    print(f" Local IP : {local_ip}")
    print(f" Port     : {PORT}")
    print(f" OS       : {platform.system()} {platform.release()} ({platform.machine()})")
    print("="*60)
    print(f" Access your server at: http://{local_ip}:{PORT}/")
    print("="*60)

    # Start server in the same directory
    httpd = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), CustomHandler)
    print("Server running... Press CTRL+C to stop.")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
