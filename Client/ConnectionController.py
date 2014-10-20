import socket
from ConnectionGUI import *
from UsernameGUI import *

class ConnectionController():

  def __init__(self):

    self.isConnected = False

    self.connectionGUI = ConnectionGUI()
    self.connectionGUI.setControllerCallback(self.connectToServer)

    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    self.connectionGUI.displayWindow()

  def connectToServer(self, ipAddress, port):
    try:
      #Connect to the server
      self.sock.connect((ipAddress, port))

      #Successfully connected, set flag
      self.isConnected = True

      #TODO: If successfully able to connect, handle the connection now

      #Done with the connection gui, remove it
      self.connectionGUI.close()

      self.askForUsername()
    except IOError as e:
      self.connectionGUI.displayError(e.strerror)
      return
    finally:
      if(self.isConnected):
        self.sock.close()

  def askForUsername(self):
    self.usernameGUI = UsernameGUI()
    self.usernameGUI.setControllerCallback(self.setUsername)
    self.usernameGUI.displayWindow()

  def setUsername(self, username):
    self.sock.send(("username " + username).encode())

if __name__ == '__main__':
  ConnectionController()