import socketserver
import sys

class ServerHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).decode()

        for word in self.data.split():
            print("Got word ", word)
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper().encode())

def main():
    if(len(sys.argv) < 2):
        print("Please specify port")
        return

    host = "localhost"
    port = None
    try:
        port = int(sys.argv[1])
    except ValueError:
        print("Enter valid port number")
        return

    # Create the server
    server = None
    try:
        server = socketserver.TCPServer((host, port), ServerHandler)
    except IOError as e:
        print(e.strerror)
        return

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

if __name__ == "__main__":
    main()

