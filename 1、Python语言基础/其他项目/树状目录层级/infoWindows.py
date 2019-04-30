import tkinter

class InfoWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.grid(row=0, column=1, ipady=5)

        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame, textvariable=self.ev, width=80)
        self.entry.pack(pady=0, side=tkinter.TOP)

        self.text = tkinter.Text(frame, width=80, height=30)
        self.text.pack(side=tkinter.BOTTOM)