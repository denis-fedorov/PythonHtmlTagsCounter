from tkinter import *
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

from validator import Validator
from requester import Requester
from tagCounter import TagCounter


class Gui:
    def __init__(self, master):
        self.separator = "========================"

        # 1. common settings
        self.master = master
        self.master.title("HTML-tags ultimate counter")
        self.master.geometry("500x300")

        # 2. frames
        self.upperFrame = Frame(self.master)
        self.outputFrame = Frame(self.master)
        self.bottomFrame = Frame(self.master)

        # 3. controls
        # 3.1 upper frame
        self.labelUrl = Label(self.upperFrame, text="URL:")
        defaulturl = StringVar(self.upperFrame, value="https://google.com")
        self.urlEntry = Entry(self.upperFrame, textvariable=defaulturl, justify=LEFT)
        self.runButton = Button(self.upperFrame, text="Run", command=self.run)
        # 3.2 output frame
        self.outputText = ScrolledText(self.outputFrame, wrap=WORD)
        # 3.3 buttom frame
        self.saveToDbButton = Button(self.bottomFrame, text="Save to DB", justify=LEFT, command=self.save_to_db)
        self.loadFromDbButton = Button(self.bottomFrame, text="Load from DB", justify=LEFT, command=self.load_from_db)
        self.exitButton = Button(self.bottomFrame, text="Exit", justify=RIGHT, command=self.exit)

        # 4. frames layout
        self.upperFrame.pack(side=TOP, fill=X)
        self.bottomFrame.pack(side=BOTTOM, fill=X)
        self.outputFrame.pack(expand=True, fill=BOTH)

        # 5. controls layout
        # 5.1 upper frame
        self.labelUrl.pack(side=LEFT)
        self.runButton.pack(side=RIGHT)
        self.urlEntry.pack(fill=X)
        # 5.2 output frame
        self.outputText.pack(side=TOP, expand=True, fill=BOTH)
        # 5.3 bottom frame
        self.saveToDbButton.pack(side=LEFT)
        self.loadFromDbButton.pack(side=LEFT)
        self.exitButton.pack(side=RIGHT)

    def run(self):
        self.clear_output()
        self.append_datetime_to_output()

        url = self.urlEntry.get()
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

    def exit(self):
        self.master.destroy()

    def save_to_db(self):
        print("Save to db in progress")
        pass

    def load_from_db(self):
        print("Load from db in progress")
        pass

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
