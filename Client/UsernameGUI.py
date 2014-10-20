import re
from tkinter import *
from tkinter.ttk import *

class UsernameGUI(Frame):

  def __init__(self):

    validPattern = "[a-zA-Z0-9]+"
    self.userNameRegex = re.compile(validPattern)

    #Create the window
    self.parent = Tk()
    self.parent.geometry("250x150+300+300")
    self.parent.resizable(width=FALSE, height=FALSE)
    Frame.__init__(self, self.parent)
    #Pack and display frame
    self.pack()

    self.initUI()

  def initUI(self):
    self.parent.title("Pick a username")
    Label(self, text="Username").pack()

    self.usernameVar = StringVar()
    vcmd = (self.parent.register(self.validateUsername), "%S", "%P")
    self.usernameInput = Entry(self, textvariable=self.usernameVar, validate = 'key', validatecommand = vcmd)
    self.usernameInput.pack()
    self.usernameInput.focus()

    self.errorMsgVar = StringVar()
    self.errorMsgLabel = Label(self, textvariable = self.errorMsgVar, wraplength = 225)
    self.errorMsgLabel.pack()

    self.usernameBtn = Button(self, text="Set Username", command=self.setUsername)
    self.usernameBtn.pack()

  def setUsername(self):
    print("Thanks for calling set username")

    possibleUsername = self.usernameInput.get()
    if(len(possibleUsername) is 0):
      displayError("Please set username")
      return

    #Have the controller set the username
    self.controllerCallback(possibleUsername)

  def displayWindow(self):
    self.parent.focus_force()
    self.parent.mainloop()

  def validateUsername(self, char, entryVal):
    if(entryVal is ""):
      return True
    if(self.userNameRegex.match(entryVal) is not None):
      if(self.userNameRegex.match(entryVal).span()[1] - self.userNameRegex.match(entryVal).span()[0] == len(entryVal)):
        return True
    return False

  def displayError(self, errorMsg):
    self.errorMsgVar.set(errorMsg)

  def setControllerCallback(self, callback):
    self.controllerCallback = callback

if __name__ == '__main__':
  gui = UsernameGUI()
  gui.displayWindow()