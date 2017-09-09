import time
from tkinter import *
from tkinter import ttk
from thepass.model.world import World


class WorldGui(object):
    def __init__(self):
        self.root = Tk()

        self.content = ttk.Frame(self.root)
        self.frame = ttk.Frame(self.content, borderwidth=5, relief="sunken", width=200, height=100)
        self.namelbl = ttk.Label(self.content, text="Name")
        self.name = ttk.Entry(self.content)

        self.NextDayButton = ttk.Button(self.content, text="Next Day")
        self.cancel = ttk.Button(self.content, text="Cancel")
        self.textbox = Text(self.content, height=40, width=80)

        self.content.grid(column=0, row=0)
        self.textbox.grid(column=0, row=1, columnspan=1, rowspan=1)
        self.namelbl.grid(column=0, row=0, columnspan=1)
        self.NextDayButton.grid(column=0, row=2, columnspan=1)
        # self.name.grid(column=3, row=1, columnspan=2)
        # self.ok.grid(column=3, row=3)
        # self.cancel.grid(column=4, row=3)

    def log(self, text):
        if text.find('\n') > 0:
            text = '\n' + text
        self.textbox.insert("end", time.ctime() + "\t" + text + "\n")
        self.textbox.see("end")

    def start(self):
        world = World(8, 8)
        world.generate()
        print(world.name)
        self.namelbl.text = world.name
        self.log(world.name)
        self.log(str(world))
        self.root.mainloop()


WorldGui().start()
