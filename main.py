from tkinter import *
from validator import Validator

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
        prefix = StringVar(self.controlFrame, value="https://")
        self.entryUrl = Entry(self.controlFrame, textvariable=prefix, justify=LEFT)
        self.buttonRun = Button(self.controlFrame, text="Run", command=self.run)
        self.outputText = Text(self.outputFrame, wrap=WORD)

        # frames layout
        self.controlFrame.pack(side=TOP, fill=X)
        self.outputFrame.pack(side=BOTTOM, expand=True, fill=BOTH)

        # controls layout
        self.labelUrl.pack(side=LEFT)
        self.buttonRun.pack(side=RIGHT)
        self.entryUrl.pack(fill=X)
        self.outputText.pack(side=TOP, expand=True, fill=BOTH)

    def run(self):
        self.outputText.delete(1.0, END)

        url = self.entryUrl.get()
        if not Validator.isurlcorrect(url):
            # error
            print("error")
            return

        print("valid")


root = Tk()
my_gui = Gui(root)
root.mainloop()
