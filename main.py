from tkinter import *
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

from validator import Validator
from requester import Requester
from tagCounter import TagCounter


class Gui:
    def __init__(self, master):
        self.separator = "========================"

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
        self.clear_output()
        self.append_datetime_to_output()

        url = self.entryUrl.get()
        if not Validator.isurlcorrect(url):
            self.append_text_to_output("Please provide a correct url")
            return

        response = Requester.send_request(url)
        state = response.key
        source = response.value

        if not state == "ok":
            self.append_text_to_output(source)
            return

        result = TagCounter.get_tags(source)
        self.append_dic_to_output(result)

    def clear_output(self):
        self.outputText.delete(1.0, END)

    def append_datetime_to_output(self):
        self.append_text_to_output(str(datetime.now().strftime("%d %B %Y, %H:%M:%S")))

    def append_text_to_output(self, text):
        self.outputText.insert(INSERT, text + "\n")

    def append_dic_to_output(self, dic):
        self.append_text_to_output(self.separator)
        self.append_text_to_output("We have found {} tags:\n".format(len(dic)))
        for tag, count in dic.items():
            self.append_text_to_output("Tag: {}, count: {}".format(tag, count))
        self.append_text_to_output(self.separator)


root = Tk()
my_gui = Gui(root)
root.mainloop()
