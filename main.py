from Graphique import *
import tkinter as tk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Login(self)
        p2 = Password(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p1.show()   

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    root.title("WAR RPG")
    main.pack(side="top", fill="both", expand=True)
    root.geometry("1400x700")
    root.mainloop()