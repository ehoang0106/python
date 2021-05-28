from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.parent = master
        self.initUI()

    def initUI(self):
        self.outputBox = Text(self.parent, bg='yellow', height= 10, fg='green', relief=SUNKEN, yscrollcommand='TRUE')
        self.outputBox.pack(fill='both', expand=True)
        self.button1 = Button(self.parent, text='button1', width=20, bg ='blue', fg='green', activebackground='black', activeforeground='green')
        self.button1.pack(side=RIGHT, padx=5, pady=5)
        self.button2 = Button(self.parent, text='button2', width=25, bg='white', fg='green', activebackground='black', activeforeground='green')
        self.button2.pack(side=LEFT, padx=5, pady=5)

def main():
    root = Tk()
    app = Application(root)
    app.parent.geometry('300x200+100+100')
    app.parent.configure(background = 'red')
    app.mainloop()

main()