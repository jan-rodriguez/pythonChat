from tkinter import *
from tkinter.ttk import *

class ConnectionGUI(Frame):

  def __init__(self):

    #Create the window
    self.parent = Tk()
    self.parent.geometry("250x150+300+300")
    self.parent.resizable(width=FALSE, height=FALSE)
    Frame.__init__(self, self.parent)
    #Pack and display frame
    self.pack()

    self.initUI()

  def initUI(self):

    self.parent.title("PY IM")

    #Button used to connect to server
    setPortBtn = Button(self, text="Connect", command=self.connectToServer)
    setPortBtn.pack(side=BOTTOM)

    ipLable = Label(self, text="IP Address")
    ipLable.pack()

    self.ipInputVar = StringVar()
    self.ipInput = Entry(self, textvariable = self.ipInputVar)
    self.ipInput.pack()
    self.ipInput.focus()

    portLabel = Label(self, text="Port")
    portLabel.pack()

    #Input for user to specify port f ip
    vcmd = (self.parent.register(self.validatePort), "%S", "%P")
    self.portInputVar = StringVar()
    self.portInput = Entry(self, textvariable = self.portInputVar, validate = 'key', validatecommand = vcmd)
    self.portInput.pack()

    self.errorMsgVar = StringVar()
    self.errorMsgLabel = Label(self, textvariable = self.errorMsgVar, wraplength = 225)
    self.errorMsgLabel.pack()

  def displayWindow(self):
    self.parent.mainloop()

  def connectToServer(self):
    ipAddress = self.ipInput.get()
    port = self.portInput.get()

    #Have to input ipaddress and port
    if(len(ipAddress) == 0):
        self.displayError("Enter an ip address")
        self.ipInput.focus()
        return
    if(len(port) == 0):
        self.displayError("Enter an port number")
        self.portInput.focus()
        return

    try:
        port = int(self.portInput.get())
        if(port < 0 or port > 65535):
            self.portInput.focus()
            self.displayError("Invalid port number")
            return

    except ValueError:
        self.portInput.focus()
        self.displayError("Invalid port number")
        return

    self.controllerCallback(ipAddress, port)

  def setControllerCallback(self, callback):
    self.controllerCallback = callback

  """
  Assure that input value for the port is a valid port number.
  Doesn't allow non-integer inputs and values
  that are too small or large to be ports.
  """
  def validatePort(self, char, entryVal):
    if(char in '0123456789' or entryVal is ""):
        if(entryVal is "" or (int(entryVal) >= 0  and int(entryVal) <= 65535)):
            return True
    return False

  def displayError(self, errorMsg):
    self.errorMsgVar.set(errorMsg)

  def close(self):
    self.quit()
    self.parent.destroy()