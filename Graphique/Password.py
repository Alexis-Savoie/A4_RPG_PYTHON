import tkinter as tk
from PIL import ImageTk
from .Page import *


class Password(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # Frame
        self.bg = ImageTk.PhotoImage(file="./img/bg2.jpg")
        self.bg_image=tk.Label(self, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #color
        Blanc="#fff"
        Gris="#fff"
        Noir="#000"
        Police="Impact"
        # Frame Login
        BlockLogin=tk.Frame(self,bg=Blanc)
        BlockLogin.place(x=100,y=500,height=400, width=700)
        tk.Label(BlockLogin, text="Forgot Password", font=(Police, 55, "bold"), fg="#bfb557", bg=Blanc).place(x=100,y=10)
        tk.Label(BlockLogin, text="Your email of deception", font=(Police, 25, "bold"), fg="#bfb557", bg=Blanc).place(x=180,y=100)
        tk.Label(BlockLogin, text="Email", font=(Police, 20, "bold"), fg=Noir, bg=Blanc).place(x=90,y=170)
        self.InputEmail=tk.Entry(BlockLogin, font=(Police, 15),text="email", bg=Gris, bd=0)
        self.InputEmail.place(x=90,y=230)
        tk.Button(self, font=(Police, 30),command=self.alert,text="Email",cursor="pirate", bg="#bfb557", bd=0,fg=Blanc).place(x=350,y=870)
        
    def alert(self):
        if self.InputEmail.get() == "":
            tk.messagebox.showerror('error', "email invalide")
        elif self.InputEmail.get() == "votre@email.com":
            tk.messagebox.showerror('error', "email invalide")
        else:
            tk.messagebox.showerror('success', "Super")


            

if __name__ == "__main__":
    root=Tk()
    obj=Password(root)
    root.mainloop()