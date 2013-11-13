from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class Dump(BaseHTTPRequestHandler):
    """Dump HTTP Requests"""

    def do_GET(self):
        self.pack_print()

    def do_POST(self):
        self.pack_print()

    def do_PUT(self):
        self.pack_print()

    def do_PATCH(self):
        self.pack_print()

    def do_DELETE(self):
        self.pack_print()

    def do_COPY(self):
        self.pack_print()

    def do_HEAD(self):
        self.pack_print()

    def do_OPTIONS(self):
        self.pack_print()

    def do_LINK(self):
        self.pack_print()

    def do_UNLINK(self):
        self.pack_print()

    def do_PURGE(self):
        self.pack_print()

    def send200(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    
    def pack_print(self):
        self.send200()
        print "***** HEADERS *****"
        print self.headers
        if 'Content-Length' in self.headers:
            len = int(self.headers['Content-Length'])
            if len > 0:
                print "***** BODY *****"
                print self.rfile.read(len).decode('utf-8')

if __name__ == '__main__':
    PORT = 8200
    try:
        httpd = HTTPServer(('',PORT), Dump)
        print 'Server started on port ',PORT
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        httpd.socket.close()