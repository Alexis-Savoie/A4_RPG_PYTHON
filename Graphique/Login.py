from tkinter import messagebox
from tkinter import *
from PIL import ImageTk

class Login:
    def __init__(self, root):
        # Frame
        self.root = root
        self.root.title("WAR RPG")
        self.root.geometry("1600x600")
        self.bg = ImageTk.PhotoImage(file="../img/bg.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #color
        Blanc="#fff"
        Gris="#fff"
        Noir="#000"
        Police="Impact"
        # Frame Login
        BlockLogin=Frame(self.root,bg=Blanc)
        BlockLogin.place(x=100,y=300,height=500, width=700)
        Label(BlockLogin, text="Connexion", font=(Police, 55, "bold"), fg="#bfb557", bg=Blanc).place(x=180,y=10)
        Label(BlockLogin, text="To back young deception", font=(Police, 25, "bold"), fg="#bfb557", bg=Blanc).place(x=180,y=100)
        Label(BlockLogin, text="Username", font=(Police, 20, "bold"), fg=Noir, bg=Blanc).place(x=90,y=170)
        self.InputEmail=Entry(BlockLogin, font=(Police, 15),text="email", bg=Gris, bd=0)
        self.InputEmail.insert(0, "votre@email.com")
        self.InputEmail.place(x=90,y=230)
        Label(BlockLogin, text="Password", font=(Police, 20, "bold"), fg=Noir, bg=Blanc).place(x=90,y=300)
        self.InputPassword=Entry(BlockLogin, font=(Police, 15),show="*",text="password", bg=Gris, bd=0)
        self.InputPassword.insert(0, "password")
        self.InputPassword.place(x=90,y=350)
        Button(BlockLogin, font=(Police, 15),text="forgot password ?", bg=Blanc, bd=0).place(x=400,y=400)
        Button(self.root, font=(Police, 30),command=self.alert,text="go to war",cursor="pirate", bg="#bfb557", bd=0,fg=Blanc).place(x=350,y=750)
        
    def alert(self):
        if self.InputEmail.get() == "" or self.InputPassword.get() == "":
            messagebox.showerror('error', "email / password invalide")
        elif self.InputEmail.get() == "votre@emai.com" or self.InputPassword.get() == "password":
            messagebox.showerror('error', "email / password invalide")
        else:
            messagebox.showerror('success', "Super")


            

        
root=Tk()
obj=Login(root)
root.mainloop()