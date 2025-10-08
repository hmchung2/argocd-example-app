from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
print("good")
PORT = int(os.getenv("PORT", "8080"))
class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers(); self.wfile.write(b"ok\n")
HTTPServer(("", PORT), H).serve_forever()