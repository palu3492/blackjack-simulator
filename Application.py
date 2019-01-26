import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # self.pack()
        self.setup()
        # Create frame to hold everything
        self.content = tk.Frame(self.master, bg='#ffffff')
        self.content.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        # self.create_widgets()
        # Create top menu bar
        self.create_main_bar()
        # Create header frames for titles
        self.create_sub_bar(0, 1)
        self.create_sub_bar(1, 1)
        self.create_settings_frame(0,2)
        self.create_settings_frame(1,2)
        self.create_sub_bar(0, 3)
        self.create_sub_bar(1, 3)
        self.create_settings_frame(0,4)
        self.create_settings_frame(1,4)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.content.columnconfigure(0, weight=1)
        self.content.columnconfigure(1, weight=1)

        self.content.rowconfigure(0, weight=1)
        self.content.rowconfigure(1, weight=1)
        self.content.rowconfigure(2, weight=1)
        self.content.rowconfigure(3, weight=1)
        self.content.rowconfigure(4, weight=1)

    def setup(self):
        self.master.title("Blackjack Simulator")
        self.master.minsize(width=1000, height=666)
        self.master.maxsize(width=1000, height=666)
        # self.master.configure(bg='#00ff60')

    #frame that holds components in the red top bar
    def create_main_bar(self):
        top = tk.Frame(self.content, bg='#222222', height=48)
        top.grid(column=0, row=0, columnspan=2, rowspan=1, sticky=(tk.E, tk.W))

    def create_sub_bar(self, col, row):
        top = tk.Frame(self.content, bg='#e1e1e1', height=35)
        top.grid(column=col, row=row, columnspan=1, rowspan=1, sticky=(tk.E, tk.W))

    def create_settings_frame(self, col, row):
        top = tk.Frame(self.content, bg='#ff0000')
        top.grid(column=col, row=row, columnspan=1, rowspan=1, sticky=(tk.N, tk.S, tk.E, tk.W))

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()