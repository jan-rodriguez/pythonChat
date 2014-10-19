from tkinter import *
from tkinter.ttk import *

class ClientUI(Frame):

  def __init__(self, parent):
    Frame.__init__(self, parent) #Initialize the frame
    self.pack() #Display the frame
    self.parent = parent

    self.initUI()   

  def initUI(self):

    self.parent.title("PY-OH-EL IM")

    #Button used to connect to server
    setPortBtn = Button(self, text="Connect", command=self.connectToServer)
    setPortBtn.pack(side=BOTTOM)

    ipLable = Label(self, text="IP Address")
    ipLable.pack()

    self.ipInput = Entry(self)
    self.ipInput.pack()

    portLabel = Label(self, text="Port")
    portLabel.pack()

    #Input for user to specify port of ip
    self.portInput = Entry(self)
    self.portInput.pack()

  def connectToServer(self):
    ipAddress = self.ipInput.get()
    port = self.portInput.get()

def main():

  root = Tk()
  root.geometry("250x150+300+300")
  app = ClientUI(root)
  root.mainloop()


if __name__ == '__main__':
  main()