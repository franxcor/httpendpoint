from http.server import BaseHTTPRequestHandler, HTTPServer
#import time
hostName = "localhost"
serverPort = 8080

import psycopg2




class BasicServer(BaseHTTPRequestHandler):
    def connect(self) :
        conn = None
        try:  
            print("connecting")
            conn = psycopg2.connect(
                dbname="postgres", #this is database name not table name
                user="postgres",
                password="Temporary123",
                host="localhost"
            )

            #cursor for statements
            cur = conn.cursor()

            cur.execute('SELECT imsi FROM subscribers;') #execute to do the actual SQL commands
            fetchedData = cur.fetchall() #fetchall to fetch the data from the SQL command
            print(fetchedData)
        except (psycopg2.DatabaseError) as error :
            print(error) #in case there is an error in the database
        finally:
            if conn is not None:
                conn.close() #closing the database connection
                print('Database connection closed')

    def do_GET(self):
        self.send_response(200) #status code for a successful request
        self.send_header("Content-type", "text/html") #adds header data to http response (name of header and value)
        self.end_headers()
        self.connect()

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
