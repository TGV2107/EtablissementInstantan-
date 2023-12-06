import tkinter as TK, tkinter
import Elements as El
import bcrypt as bc

class Window:
    def __init__(self,name,size:str, items:list, minsize:tuple= None, maxsize:tuple= None, bg:str="white", logopath:str= None) -> None:
        self.name = name
        self.size = size
        self.items = items
        self.minsize = minsize
        self.maxsize = maxsize
        self.bg = bg
        self.logopath = logopath
        self.palet = ("#CAF0F8","#90E0EF","#48CAE4","#00B4D8","#0096C7","#0077B6","#03045E") 

    def __str__(self) -> str:
        return ("Fenetre " + self.name + " de taille " + self.size)

    def show(self):
        window = tkinter.Tk()
        window.geometry(self.size)
        window.title(self.name)
        window.config(background="Black")
        frame.pack()
        window.mainloop()

password =""
maincolor = ("#CAF0F8","#90E0EF","#48CAE4","#00B4D8","#0096C7","#0077B6","#03045E")
widthentry = 30
window = tkinter.Tk()
window.geometry("400x600")
window.minsize(300,550)
window.title("Page de Connection")
window.config(background=maincolor[0], bd=0)
bullet = "\u25CF"
window.tk.call("wm", "iconphoto", window._w, tkinter.PhotoImage(file="./Assets/IMG/ESI_Logo.ico"))

frame = tkinter.Frame(window,bg=maincolor[0])
titleframe = tkinter.Frame(window,bg= maincolor[0])


def verify(password):
    """Watch if the Crypted Password is the same as the crypted Password on the Data Base"""
    password = password.encode("utf-8")
    hashedpassword = bc.hashpw(password,bc.gensalt(10))
    return window.destroy




Frame = El.Frame(bg = maincolor[0])

Frame.items = [El.Images("./Assets/IMG/ESI_Logo.png",300,200,maincolor[0],anchor=tkinter.CENTER,expand=tkinter.YES)]

Frame2 = El.Frame(bg = maincolor[0],expand=TK.YES)
Frame2.items = [El.Label(text="Connectez vous : ", font=("Helvetica",30), bg = maincolor[0]),
                    El.Label(text="Entrez votre Identifiant :", font=("Helvetica",15),bg= maincolor[0],pady=10),
                    El.Entry(width=30,font=("Helvetica",10)),
                    El.Label(text="Entrez votre mot de passe :", font= ("Helvetica", 15),bg = maincolor[0],pady=10),
                    El.Entry(width=30, font=("Helvetica",10), show= bullet, textvariable= password),
                    El.Button(text="Valider",font=("Helvetica",15),bg=maincolor[3],command=verify(password),pady=10),
                    El.Button(text="Créer un compte",font=("Helvetica",15),bg=maincolor[3],pady = 10),
                    El.Button(text="Mot de passe oublié ?",font=("Helvetica",10),bg= maincolor[1], pady=5)]

Frame.pack(window)
Frame2.pack(window)
window.mainloop()