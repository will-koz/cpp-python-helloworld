# Start the most basic of http servers using python
# Go to localhost:12345

from http.server import BaseHTTPRequestHandler, HTTPServer

class Server (BaseHTTPRequestHandler):
	def do_GET (self):
		response_code = 200 # No errors. Everything served correctly
		response_content = b"Hello World"

		self.send_response(response_code)
		self.end_headers()
		self.wfile.write(response_content)

def start_server (port = 12345, host_name = ""):
	webserver = HTTPServer((host_name, port), Server)
	webserver.serve_forever()

if __name__ == "__main__":
	start_server()
