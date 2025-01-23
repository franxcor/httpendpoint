from http.server import BaseHTTPRequestHandler, HTTPServer
#import time
hostName = "localhost"
serverPort = 8080

import psycopg2

connection = psycopg2.connect (
    dbname="subscribers",
    user="postgres",
    password="Temporary123",
    host="localhost"
)

class BasicServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) #status code for a successful request
        self.send_header("Content-type", "text/html") #adds header data to http response (name of header and value)
        self.end_headers()

        #just content on the page
        self.wfile.write(bytes("<html><head></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p> a web server </p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
if __name__ == "__main__" :
    webServer = HTTPServer((hostName, serverPort), BasicServer) #starting the actual server
    print("Server url http://%s:%s" % (hostName, serverPort)) #creating link
    try :
        webServer.serve_forever() #keeping the terminal running
    except KeyboardInterrupt : #ctrl c in terminal
        pass

    webServer.server_close() #once keyboard interrupt, then close the webserver
    print("Server terminated")
