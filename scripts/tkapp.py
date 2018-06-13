import tkinter as tk
from tkinter import messagebox

class App(tk.Frame):
    

    def __init__(self, master=None):
        self._msgLabel=""
        tk.Frame.__init__(self,master)
        self.grid()
        self.createTopMenu()
        self.createWidgets()
    
    def createTopMenu(self):
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        top['menu'] = self.menuBar

        self.subMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label='Help', menu=self.subMenu)
        self.subMenu.add_command(label='Hello there!', command=self.hello)
        self.subMenu.add_command(label='Quit!', command=self.quit)
        #You must use the .add_cascade() method for all the items you want on the top menu bar. Calls to .add_checkbutton(), .add_command(), or .add_radiobutton() will be ignored.

    
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()
        self.msgBox = tk.Label(self, text="Oh my msgBox")
        self.msgBox.grid(row=1) # need to run grid placement on new line to preserve Label object
        #print(type(self.msgBox))


    def hello(self):
        print('Oh hello there!')
        messagebox.showinfo('Msg Title', 'Hello there indeed!')
        self._msgLabel="Hello Label active"
        self.msgBox['text']='Hello was activated'
        print(type(self.msgBox))
        #self.msgBox.configure(text='Hello was activated')
        

def main():
    app = App()
    app.master.title('My Tkinter App')
    app.mainloop()

if __name__ == "__main__":
    print(f'Running Main App')
    main()