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
        self.photo = tk.PhotoImage(file="images/logo1.png")
        self.create_main_bar()
        # Create header frames for titles
        self.create_sub_bar(0, 1, "Simulator Settings", False)
        self.create_sub_bar(1, 1, "Blackjack Game Options (House Rules)", False)
        self.create_settings_frame(0,2)
        self.create_settings_frame(1,2)
        self.create_sub_bar(0, 3, "Player Options", False)
        # Count variable
        self.count_enabled = tk.IntVar()
        self.create_sub_bar(1, 3, "Card Counting Options", True)
        self.create_settings_frame(0,4)
        self.create_settings_frame(1,4)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.content.columnconfigure(0, weight=1)
        self.content.columnconfigure(1, weight=1)

        self.content.rowconfigure(0, weight=0)
        self.content.rowconfigure(1, weight=0)
        self.content.rowconfigure(2, weight=1)
        self.content.rowconfigure(3, weight=0)
        self.content.rowconfigure(4, weight=1)

    def setup(self):
        self.master.title("Blackjack Simulator")
        self.master.minsize(width=1000, height=666)
        self.master.maxsize(width=1000, height=666)
        # self.master.configure(background='#00ff60')

    # Frame that holds components in top black bar
    def create_main_bar(self):
        top = tk.Frame(self.content, bg='#222222', height=48)
        top.grid(column=0, row=0, columnspan=2, rowspan=1, sticky=(tk.E, tk.W))
        # top.columnconfigure(0, weight=0)
        # top.columnconfigure(1, weight=0)
        top.rowconfigure(0, weight=1)
        top.grid_propagate(0)

        # Logo
        photo_label = tk.Label(top, bg="#222222", image=self.photo, width=48, height=48)
        photo_label.grid(column=0, row=0, columnspan=1, rowspan=1)

        # button = tk.Button(top)
        # self.photo = tk.PhotoImage(file="images/logo.png", width=150, height=150)
        # button.config(image=self.photo, width=48, height=48, bg='#222222', relief='flat')
        # button.grid(column=0, row=0, columnspan=1, rowspan=1, sticky=tk.W)

        # Label
        label = tk.Label(top, text="Blackjack Simulator", bg="#222222", fg="#ffffff", font=("Arial", 16), padx=0)
        label.grid(column=1, row=0, columnspan=1, rowspan=1)

    def create_sub_bar(self, col, row, title, enable):
        bar = tk.Frame(self.content, bg='#e1e1e1', height=35, borderwidth=1, relief="solid")
        bar.grid(column=col, row=row, columnspan=1, rowspan=1, sticky=(tk.E, tk.W))
        bar.grid_propagate(0)
        bar.rowconfigure(0, weight=1)

        label = tk.Label(bar, text=title, bg="#e1e1e1", fg="#000000", font=("Arial", 10), padx=10)
        label.grid(column=0, row=0, columnspan=1, rowspan=1)

        if enable:
            radio_button1 = tk.Radiobutton(bar, text="Enable", variable=self.count_enabled, value=1, command=self.print_count_varible, bg="#e1e1e1", fg="#000000", font=("Arial", 9), padx=10)
            radio_button2 = tk.Radiobutton(bar, text="Disable", variable=self.count_enabled, value=0, command=self.print_count_varible, bg="#e1e1e1", fg="#000000", font=("Arial", 9), padx=0)
            radio_button1.grid(column=1, row=0, columnspan=1, rowspan=1)
            radio_button2.grid(column=2, row=0, columnspan=1, rowspan=1)

    def print_count_varible(self):
        print(self.count_enabled.get())

    def create_settings_frame(self, col, row):
        top = tk.Frame(self.content, bg='#ffffff', borderwidth=1, relief="solid")
        top.grid(column=col, row=row, columnspan=1, rowspan=1, sticky=(tk.N, tk.S, tk.E, tk.W))

    # def create_label(self, parent):
    #     label_container = tk.Frame(parent, bg='#222222')
    #     label_container.grid(column=0, row=0, columnspan=1, rowspan=1)
    #     label_container.columnconfigure(0, weight=0)
    #     label_container.rowconfigure(0, weight=0)
    #     # Add label
    #     label = tk.Label(label_container, text="Title", bg="#ffffff", fg="#000000")
    #     label.grid(column=0, row=0, columnspan=1, rowspan=1)

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