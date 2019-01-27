import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.setup_application()


    def setup_application(self):
        self.window_setup()
        self.create_frames()
        self.add_blackjack_rules(self.blackjack_settings_frame)


    def window_setup(self):
        self.master.title("Blackjack Simulator")
        self.master.minsize(width=1000, height=666)
        # self.master.maxsize(width=1000, height=666)

    def create_frames(self):
        # Create frame to hold everything
        self.content = tk.Frame(self.master, bg='#ffffff')
        self.content.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        # self.create_widgets()
        # Create top menu bar
        self.photo1 = tk.PhotoImage(file="images/logo1.png")
        self.photo2 = tk.PhotoImage(file="images/playButton.png")
        self.create_top_bar()
        # Create header frames for titles
        self.create_sub_bar(0, 1, "Simulator Settings", False)
        self.create_sub_bar(1, 1, "Blackjack/House Rules", False)
        # self.simulator_settings_frame = self.create_settings_frame(0, 2)
        self.blackjack_settings_frame = self.create_settings_frame(1, 2)
        self.create_sub_bar(0, 3, "Player Options", False)
        # Count variable
        self.count_enabled = tk.IntVar()
        self.create_sub_bar(1, 3, "Card Counting Options", True)
        # self.player_settings_frame = self.create_settings_frame(0, 4)
        # self.counting_settings_frame = self.create_settings_frame(1, 4)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.content.columnconfigure(0, weight=1)
        self.content.columnconfigure(1, weight=1)

        self.content.rowconfigure(0, weight=0)
        self.content.rowconfigure(1, weight=0)
        self.content.rowconfigure(2, weight=1)
        self.content.rowconfigure(3, weight=0)
        self.content.rowconfigure(4, weight=1)

    # Frame that holds components in top black bar
    def create_top_bar(self):
        top = tk.Frame(self.content, bg='#222222', height=48)
        top.grid(column=0, row=0, columnspan=2, rowspan=1, sticky=(tk.E, tk.W))
        # top.columnconfigure(0, weight=0)
        # top.columnconfigure(1, weight=0)
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=0)
        top.columnconfigure(1, weight=0)
        top.columnconfigure(2, weight=1)
        top.columnconfigure(3, weight=0)
        top.grid_propagate(0)

        # Logo
        photo_label = tk.Label(top, bg="#222222", image=self.photo1, width=48, height=48)
        photo_label.grid(column=0, row=0, columnspan=1, rowspan=1)

        # Label
        label = tk.Label(top, text="Blackjack Simulator", bg="#222222", fg="#ffffff", font=("Arial", 16), padx=0)
        label.grid(column=1, row=0, columnspan=1, rowspan=1)

        # Label
        label = tk.Label(top, text="Run", bg="#222222", fg="#ffffff", font=("Arial", 12))
        label.grid(column=2, row=0, columnspan=1, rowspan=1, sticky=tk.E)

        # Play button
        button = tk.Button(top)
        button.config(image=self.photo2, width=30, height=48, bg='#222222', relief='flat')
        button.grid(column=3, row=0, columnspan=1, rowspan=1)


    def create_sub_bar(self, col, row, title, enable):
        bar = tk.Frame(self.content, bg='#fafafa', height=35, borderwidth=1, relief="solid")
        bar.grid(column=col, row=row, columnspan=1, rowspan=1, sticky=(tk.E, tk.W))
        bar.grid_propagate(0)
        bar.rowconfigure(0, weight=1)

        label = tk.Label(bar, text=title, bg="#fafafa", fg="#000000", font=("Arial", 10), padx=7)
        label.grid(column=0, row=0, columnspan=1, rowspan=1)

        if enable:
            radio_button1 = tk.Radiobutton(bar, text="Enable", variable=self.count_enabled, value=1, command=self.print_count_varible, bg="#fafafa", fg="#000000", font=("Arial", 9), padx=10)
            radio_button2 = tk.Radiobutton(bar, text="Disable", variable=self.count_enabled, value=0, command=self.print_count_varible, bg="#fafafa", fg="#000000", font=("Arial", 9), padx=0)
            radio_button1.grid(column=1, row=0, columnspan=1, rowspan=1)
            radio_button2.grid(column=2, row=0, columnspan=1, rowspan=1)

    def print_count_varible(self):
        pass
        # print(self.count_enabled.get())

    def create_settings_frame(self, col, row):
        # Create outer frame to hold Canvas and Scrollbar
        myframe = tk.Frame(self.content, bg='#ffffff', borderwidth=1, relief="solid")
        myframe.grid(column=col, row=row, columnspan=1, rowspan=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        myframe.columnconfigure(0, weight=1)
        myframe.columnconfigure(1, weight=0)
        myframe.grid_propagate(0)

        # Create canvas to hold frame of objects so frame can scroll
        self.canvas = tk.Canvas(myframe, bg='#ffffff', highlightthickness=0)
        self.canvas.grid(column=0, row=0, columnspan=1, rowspan=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.canvas.grid_propagate(0)

        # Frame for objects
        frame = tk.Frame(self.canvas, bg='#ffffff')
        # frame.columnconfigure(0, weight=1)

        # Scrollbar for inner frame but placed in outer frame
        myscrollbar = tk.Scrollbar(myframe, orient="vertical", command=self.canvas.yview) #command=self.canvas.yview
        myscrollbar.grid(column=1, row=0, columnspan=1, rowspan=1, sticky=(tk.N, tk.S))

        self.canvas.configure(yscrollcommand=myscrollbar.set)
        self.canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", self.myfunction)

        return frame

    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_blackjack_rules(self, parent):
        rule_headings = ["Double Down Rules", "Split Rules", "Surrender and Insurance Rules", "Unusual Blackjack Games", " Win/Play Variations", "Card Handling Variations", "Bonuses", "Tournament Rules"]
        row = 0
        heading_count = 0
        for heading in rule_headings:
            label = tk.Label(parent, text=heading, bg="#ffffff", fg="#000000", font=("Arial", 10, 'bold', 'underline'), padx=7)
            label.grid(column=0, row=row, columnspan=1, rowspan=1, sticky=tk.W)
            row += 1
            for i in range(2):
                label = tk.Label(parent, text="Hit after Double Down:", bg="#ffffff", fg="#000000", font=("Arial", 10), padx=7)
                label.grid(column=0, row=row, columnspan=1, rowspan=1, sticky=tk.W)
                row += 1
            heading_count += 1

        # label = tk.Label(parent, text="Double down on  [Any first two cards,  9-11 only,  10-11 only, 11 only]", bg="#ffffff", fg="#000000", font=("Arial", 10), padx=7)
        # label.grid(column=0, row=1, columnspan=1, rowspan=1, sticky=tk.W)
        # label = tk.Label(parent, text="Discard Double:", bg="#ffffff", fg="#000000", font=("Arial", 10), padx=7)
        # label.grid(column=0, row=2, columnspan=1, rowspan=1, sticky=tk.W)
        # label = tk.Label(parent, text="Hit after Double Down:", bg="#ffffff", fg="#000000", font=("Arial", 10), padx=7)
        # label.grid(column=0, row=3, columnspan=1, rowspan=1, sticky=tk.W)


root = tk.Tk()
app = Application(master=root)
app.mainloop()