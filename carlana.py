#guilmour

import SocketServer
import SimpleHTTPServer

PORTA = 80

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORTA), Handler)

print "Servidor criado na porta: ", PORTA
httpd.serve_forever()
