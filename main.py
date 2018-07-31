from tkinter import *
from tkinter.scrolledtext import ScrolledText
from datetime import datetime

from validator import Validator
from requester import Requester
from tagCounter import TagCounter
from dbWrapper import DbWrapper


class Gui:
    def __init__(self, master):
        self.separator = "========================"
        self.db_wrapper = DbWrapper()

        # 1. common settings
        self.master = master
        self.master.title("HTML-tags ultimate counter")
        self.master.geometry("500x500")

        # 2. frames
        self.upper_frame = Frame(self.master)
        self.output_frame = Frame(self.master)
        self.bottom_frame = Frame(self.master)

        # 3. controls
        # 3.1 upper frame
        self.label_url = Label(self.upper_frame, text="URL:")
        default_url = StringVar(self.upper_frame, value="https://google.com")
        self.url_entry = Entry(self.upper_frame, textvariable=default_url, justify=LEFT)
        self.run_button = Button(self.upper_frame, text="Run", command=self.run)
        # 3.2 output frame
        self.output_text = ScrolledText(self.output_frame, wrap=WORD)
        # 3.3 bottom frame
        self.save_to_db_button = Button(self.bottom_frame, text="Save to DB", justify=LEFT, command=self.save_to_db)
        self.load_from_db_button = Button(self.bottom_frame, text="Load the last record from DB", justify=LEFT,
                                          command=self.load_from_db)
        self.exit_button = Button(self.bottom_frame, text="Exit", justify=RIGHT, command=self.exit)

        # 4. frames layout
        self.upper_frame.pack(side=TOP, fill=X)
        self.bottom_frame.pack(side=BOTTOM, fill=X)
        self.output_frame.pack(expand=True, fill=BOTH)

        # 5. controls layout
        # 5.1 upper frame
        self.label_url.pack(side=LEFT)
        self.run_button.pack(side=RIGHT)
        self.url_entry.pack(fill=X)
        # 5.2 output frame
        self.output_text.pack(side=TOP, expand=True, fill=BOTH)
        # 5.3 bottom frame
        self.save_to_db_button.pack(side=LEFT)
        self.load_from_db_button.pack(side=LEFT)
        self.exit_button.pack(side=RIGHT)

    def run(self):
        self.clear_output()
        self.append_datetime_to_output()

        url = self.url_entry.get()
        if not Validator.is_url_correct(url):
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
        text_to_save = self.output_text.get("1.0", END)
        if not text_to_save.strip():
            self.append_text_to_output("Nothing to save - the result is empty")
            return

        time_stamp = datetime.now()

        try:
            self.db_wrapper.save(time_stamp, text_to_save)
        except:
            self.append_text_to_output("Can't save the result into db")
            return

        self.clear_output()
        self.append_text_to_output("The result was saved into DB")

    def load_from_db(self):
        self.clear_output()
        try:
            text = self.db_wrapper.load_last_record()
        except:
            self.append_text_to_output("Can't load the result from db")
            return

        if not text:
            self.append_text_to_output("DB is empty")
        else:
            self.append_text_to_output("The result was loaded from DB:\n{}".format(text))

    def clear_output(self):
        self.output_text.delete(1.0, END)

    def append_datetime_to_output(self):
        self.append_text_to_output(str(datetime.now().strftime("%d %B %Y, %H:%M:%S")))

    def append_text_to_output(self, text):
        self.output_text.insert(INSERT, text + "\n")

    def append_dic_to_output(self, dic):
        self.append_text_to_output(self.separator)
        self.append_text_to_output("We have found {} tags:\n".format(len(dic)))
        for tag, count in dic.items():
            self.append_text_to_output("Tag: {}, count: {}".format(tag, count))
        self.append_text_to_output(self.separator)


root = Tk()
my_gui = Gui(root)
root.mainloop()
