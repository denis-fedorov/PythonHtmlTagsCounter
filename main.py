from tkinter import *
from tkinter.scrolledtext import ScrolledText
from validator import Validator
from requester import Requester
from datetime import datetime


class Gui:
    def __init__(self, master):
        # common settings
        self.master = master
        self.master.title("HTML-tags ultimate counter")
        self.master.geometry("500x300")

        # frames
        self.controlFrame = Frame(self.master)
        self.outputFrame = Frame(self.master)
        self.closeFrame = Frame(self.master)

        # controls
        self.labelUrl = Label(self.controlFrame, text="URL:")
        defaulturl = StringVar(self.controlFrame, value="https://google.com")
        self.entryUrl = Entry(self.controlFrame, textvariable=defaulturl, justify=LEFT)
        self.buttonRun = Button(self.controlFrame, text="Run", command=self.run)
        self.outputText = ScrolledText(self.outputFrame, wrap=WORD)

        # frames layout
        self.controlFrame.pack(side=TOP, fill=X)
        self.outputFrame.pack(side=BOTTOM, expand=True, fill=BOTH)

        # controls layout
        self.labelUrl.pack(side=LEFT)
        self.buttonRun.pack(side=RIGHT)
        self.entryUrl.pack(fill=X)
        self.outputText.pack(side=TOP, expand=True, fill=BOTH)

    def run(self):
        self.clearOutput()
        self.showDateTimeInOutput()

        url = self.entryUrl.get()
        if not Validator.isurlcorrect(url):
            self.appendToOutput("Please provide a correct url")
            return

        response = Requester.sendRequest(url)
        state = response[0]
        message = response[1]

        self.appendToOutput(message)

        if not state == "ok":
            return

    def clearOutput(self):
        self.outputText.delete(1.0, END)

    def showDateTimeInOutput(self):
        self.appendToOutput(str(datetime.now().strftime("%d %B %Y, %H:%M:%S")))

    def appendToOutput(self, text):
        self.outputText.insert(INSERT, text + "\n")
        pass


root = Tk()
my_gui = Gui(root)
root.mainloop()
