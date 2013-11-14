from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import argparse

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

def create_cmdarg():
    parser = argparse.ArgumentParser(description='Request Dumper')
    parser.add_argument('-a','--address',help='Address to listen to',default='')
    parser.add_argument('-p','--port', type=int, help='Port to listen to',default=8080)
    args = parser.parse_args()
    return (args.address,args.port)

if __name__ == '__main__':
    ADDR,PORT = create_cmdarg()
    try:
        httpd = HTTPServer((ADDR,PORT), Dump)
        print('Server started on %s:%s' % (httpd.server_address))
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        httpd.socket.close()