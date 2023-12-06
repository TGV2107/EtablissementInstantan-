import tkinter

class Window:
    def __init__(self,name,size,font) -> None:
        self.name = name
        self.size = size
        self.font = font
        

    def __str__(self) -> str:
        return ("Fenetre " + self.name + " De taille " + self.size)

    def display(self):
        pass

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

frame = tkinter.Frame(window,bg=maincolor[0])
titleframe = tkinter.Frame(window,bg= maincolor[0])

title = tkinter.Label(titleframe,text="Etablissement\nScolaire\nInstantané",font=("Helevetica",35),bg=maincolor[0])
title.pack(padx=30,fill=tkinter.X)


connected = tkinter.Label(frame, text="Connectez-vous :",font=("Helvetica",30), bg=maincolor[0])
connected.pack()

pseudotxt = tkinter.Label(frame,text="Entrez votre Identifiant :",font=("Helvetica",15),bg= maincolor[0])
pseudotxt.pack(pady=10, fill=tkinter.X)

pseudo = tkinter.Entry(frame, width=widthentry,font=("Helvetica",10))
pseudo.pack()

passwordtxt = tkinter.Label(frame,text="Entrez votre mot de passe :",font=("Helvetica",15),bg= maincolor[0])
passwordtxt.pack(pady=10,fill=tkinter.X)

password = tkinter.Entry(frame,show=bullet, width=widthentry,font=("Helvetica",10))
password.pack()

valider = tkinter.Button(frame,text="Valider",font=("Helvetica",15),bg=maincolor[3],command=window.destroy)
valider.pack(pady=10)

signin = tkinter.Button(frame,text="Créer un compte",font=("Helvetica",15),bg=maincolor[3])
signin.pack(pady=10)

passwordunknown = tkinter.Button(frame,text="Mot de passe oublié ?",font=("Helvetica",10),bg= maincolor[1])
passwordunknown.pack(pady=5)

titleframe.pack(side = tkinter.TOP)
frame.pack(expand= tkinter.YES)
window.mainloop()
