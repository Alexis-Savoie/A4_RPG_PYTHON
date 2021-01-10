import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from .Page import *
from .Password import *


class Login(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # Frame
        # self = root
        #self.geometry("1600x600")
        self.bg = ImageTk.PhotoImage(file="./img/bg.jpg")
        tk.Label(self, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #color
        Blanc="#fff"
        Gris="#fff"
        Noir="#000"
        Police="Impact"
        # Frame Login
        BlockLogin=tk.Frame(self,bg=Blanc)
        BlockLogin.place(x=100,y=300,height=500, width=700)
        tk.Label(BlockLogin, text="Connexion", font=(Police, 55, "bold"), fg="#bfb557", bg=Blanc).place(x=180,y=10)
        tk.Label(BlockLogin, text="To back young deception", font=(Police, 25, "bold"), fg="#bfb557", bg=Blanc).place(x=180,y=100)
        tk.Label(BlockLogin, text="Email", font=(Police, 20, "bold"), fg=Noir, bg=Blanc).place(x=90,y=170)
        self.InputEmail=tk.Entry(BlockLogin, font=(Police, 15),text="email", bg=Gris, bd=0)
        self.InputEmail.place(x=90,y=230)
        tk.Label(BlockLogin, text="Password", font=(Police, 20, "bold"), fg=Noir, bg=Blanc).place(x=90,y=300)
        self.InputPassword=tk.Entry(BlockLogin, font=(Police, 15),show="*",text="password", bg=Gris, bd=0)
        self.InputPassword.insert(0, "password")
        self.InputPassword.place(x=90,y=350)
        tk.Button(BlockLogin, font=(Police, 15),command=Password(self).lift, text="forgot password ?", bg=Blanc, bd=0).place(x=400,y=400)
        tk.Button(self, font=(Police, 30),command=self.alert,text="go to war",cursor="pirate", bg="#bfb557", bd=0,fg=Blanc).place(x=350,y=750)
        
    def alert(self):
        if self.InputEmail.get() == "" or self.InputPassword.get() == "":
            messagebox.showerror('error', "email / password invalide")
        elif self.InputEmail.get() == "votre@emai.com" or self.InputPassword.get() == "password":
            messagebox.showerror('error', "email / password invalide")
        else:
            messagebox.showinfo('warning', "Super")


                
# if __name__ == "__main__": 
#     root=Tk()
#     obj=Login(root)
#     root.mainloop()