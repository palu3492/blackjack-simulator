from tkinter import *
master = Tk()
master.title("Blackjack Simulator")
master.minsize(width=1000, height=666)
master.maxsize(width=1000, height=666)
master.configure(bg='#ffffff')
mainloop()
#222222





# class Application(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
#         self.grid()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.quitButton = tk.Button(self, text='Quit', command=self.quit)
#         self.quitButton.grid()
#
# app = Application()
# app.master.title('Sample application')
# app.mainloop()