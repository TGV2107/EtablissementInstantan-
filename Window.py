import tkinter as TK, tkinter
import Elements as El
from PIL import Image, ImageTk
import bcrypt as bc

class Window:
    def __init__(self,name,size,font) -> None:
        self.name = name
        self.size = size
        self.font = font

        self.items = []
        

    def __str__(self) -> str:
        return ("Fenetre " + self.name + " de taille " + self.size)

    def show(self):
        window = tkinter.Tk()
        window.geometry(self.size)
        window.title(self.name)
        window.config(background="Black")
        frame = tkinter.Frame(window,bg="Black",bd=1)
        label = tkinter.Label(frame, text="Etablissement Scolaire Instantané",font=self.font)
        label.pack()
        frame.pack()
        window.mainloop()

maincolor = ("#CAF0F8","#90E0EF","#48CAE4","#00B4D8","#0096C7","#0077B6","#03045E")
widthentry = 30
window = tkinter.Tk()
window.geometry("400x600")
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


#title = tkinter.Label(titleframe,text="Etablissement\nScolaire\nInstantané",font=("Helevetica",35),bg=maincolor[0])
#title.pack(padx=30,fill=tkinter.X)
pseudo = ""
password = ""
width = 300
height = 200
img = Image.open("./Assets/IMG/ESI_Logo.png")
resized_image = img.resize((width, height), Image.ANTIALIAS)
tkinter_image = ImageTk.PhotoImage(resized_image)
canvas = tkinter.Canvas(titleframe,width=width, height= height,bg= maincolor[0],highlightthickness=0)
canvas.create_image(width/2, height/2, anchor=tkinter.CENTER, image=tkinter_image)
canvas.pack(expand=tkinter.YES)


connected = tkinter.Label(frame, text="Connectez-vous :",font=("Helvetica",30), bg=maincolor[0])
connected.pack()

idtxt = tkinter.Label(frame,text="Entrez votre Identifiant :",textvariable = pseudo, font=("Helvetica",15),bg= maincolor[0])
idtxt.pack(pady=10, fill=tkinter.X)

id = tkinter.Entry(frame, width=widthentry,font=("Helvetica",10))
id.pack()

passwordtxt = tkinter.Label(frame,text="Entrez votre mot de passe :",textvariable=password,font=("Helvetica",15),bg= maincolor[0])
passwordtxt.pack(pady=10,fill=tkinter.X)

pword = tkinter.Entry(frame,show=bullet, width=widthentry,font=("Helvetica",10))
pword.pack()

valider = tkinter.Button(frame,text="Valider",font=("Helvetica",15),bg=maincolor[3],command=verify(password))
valider.pack(pady=10)

signin = tkinter.Button(frame,text="Créer un compte",font=("Helvetica",15),bg=maincolor[3])
signin.pack(pady=10)

passwordunknown = tkinter.Button(frame,text="Mot de passe oublié ?",font=("Helvetica",10),bg= maincolor[1])
passwordunknown.pack(pady=5)

titleframe.pack(side = tkinter.TOP)
frame.pack(expand= tkinter.YES)
window.mainloop()


window2 = tkinter.Tk()
window2.geometry("400x600")
window2.title("Le caca")
window2.config(bg = maincolor[0])

FrameTest = El.Frame(bg = maincolor[0])

FrameTest.items = [El.Label(text="Etablissement\nScolaire\nInstantané", bg= maincolor[0])]

FrameTest2 = El.Frame(bg = maincolor[0],expand=TK.YES)
FrameTest2.items = [El.Label(text="Connectez vous : ", font=("Helvetica",15), bg = maincolor[0]),
                    El.Label(text="Entrez votre Identifiant :", font=("Helvetica",15),bg= maincolor[0],pady=10),
                    El.Label(text="Entrez votre mot de passe", font= ("Helvetica", 15),bg = maincolor[0],pady=10),
                    El.Label(text="Autre",font= ("Helvetica",15),bg = maincolor[0])]

FrameTest.pack(window2)
FrameTest2.pack(window2)
window2.mainloop()