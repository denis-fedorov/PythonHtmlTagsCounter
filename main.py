from tkinter import *


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
        self.entryUrl = Entry(self.controlFrame, justify=LEFT)
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
        print("DO SOMETHING")
        self.outputText.delete(1.0, END)
        pass


root = Tk()
my_gui = Gui(root)
root.mainloop()
