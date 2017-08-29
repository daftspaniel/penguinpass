import time
import tkinter as tk

from thepass.model.world import World

world = World()


class Viewer(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.build_Gui()
        world.generate()
        self.log(world.name)
        self.log(str(world))

    def build_Gui(self):
        self.text = tk.Text(self, height=160, width=100)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

    def log(self, text):
        self.text.insert("end", time.ctime() + "\t" + text + "\n")
        self.text.see("end")


if __name__ == "__main__":
    root = tk.Tk()
    frame = Viewer(root)
    frame.pack(fill="both", expand=True)
    root.mainloop()
