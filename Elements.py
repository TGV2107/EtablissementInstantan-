import tkinter as tk
import PIL
from PIL import Image, ImageTk


class Label:

    def __init__(self, text : str, font : tuple = ("Helvetica", 35), bg : str = "Black", pady : int = 0, padx : int = 0, fill = None, expand = tk.NO) -> None:
        
        self.text = text
        self.font = font
        self. bg = bg
        self.pady = pady
        self.padx = padx
        self.fill = fill
        self.expand = expand
        

    def __str__(self) -> str:
        return self.text

    def pack(self, master):

        label = tk.Label(master, text=self.text, font=self.font, bg=self.bg)
        label.pack(pady=self.pady, padx=self.padx, fill=self.fill, expand=self.expand)


class Button:

    def __init__(self, text:str, font:tuple =("Helvetica",15),bg= "White", command= None, textvariable:str=None,pady:int = 0,padx:int = 0,fill= None,expand= tk.NO) -> None:
        self.text = text
        self.font = font
        self.bg = bg
        self.command = command
        self.textvariable = textvariable
        self.pady = pady
        self.padx = padx
        self.fill = fill
        self.expand = expand
    
    def __str__(self) -> str:
        return "Button " + self.text

    def pack(self, master):
        button = tk.Button(master,text= self.text, font= self.font, bg= self.bg, textvariable= self.textvariable, command=self.command)
        button.pack(pady=self.pady, padx=self.padx, fill=self.fill, expand=self.expand)

class Entry:

    def __init__(self, width:int,font:tuple =("Helvetica",15),show:str ="",textvariable:int=None, pady:int = 0,padx:int = 0,fill= None,expand= tk.NO) -> None:
        self.width = width
        self.font = font
        self.show = show
        self.textvariable = textvariable
        self.pady = pady
        self.padx = padx
        self.fill = fill
        self.expand = expand
        
    def __str__(self) -> str:
        return "Input Box"
    
    def pack(self, master):
        entry = tk.Entry(master, width= self.width, font= self.font, show= self.show, textvariable= self.textvariable)
        entry.pack(pady= self.pady, padx= self.padx, fill= self.fill, expand= self.expand)
        

class Canvas:

    def __init__(self, width:int, height:int,bg:str, highlightthickness:int=0,pady:int = 0,padx:int = 0,fill= None,expand= tk.NO) -> None:
        self.width = width
        self.height = height
        self.bg = bg
        self.highlightthickness = highlightthickness
        self.pady = pady
        self.padx = padx
        self.fill = fill
        self.expand = expand
    
    def __str__(self) -> str:
        return "Canvas"
    
    def pack(self, master):
        canvas = tk.Canvas(master, width=self.width, height= self.height, bg= self.bg, highlightthickness= self.highlightthickness)
        canvas.pack(pady=self.pady, padx= self.padx, fill= self.fill, expand= self.expand)

class Images:

    def __init__(self, path:str, width:int, height:int, bg: str, highlightthickness:int=0, pady:int=0, padx:int=0, fill=None, expand=tk.NO, anchor=None) -> None:
        self.path = path
        self.width = width
        self.height = height
        self.bg = bg
        self.pady = pady
        self.padx = padx
        self.highlightthickness = highlightthickness
        self.fill = fill
        self.expand = expand
        self.anchor = anchor
        self.tkinter_image = None  # Ajoutez cette ligne

    def __str__(self) -> str:
        return "Image"

    def pack(self, master):
        img = Image.open(self.path)
        resized_image = img.resize((self.width, self.height), Image.ANTIALIAS)
        self.tkinter_image = ImageTk.PhotoImage(resized_image)  # Modifiez cette ligne
        canvas = tk.Canvas(master, width=self.width, height=self.height, bg=self.bg, highlightthickness=self.highlightthickness)
        canvas.create_image(self.width/2, self.height/2, anchor=self.anchor, image=self.tkinter_image)
        canvas.pack(pady=self.pady, padx=self.padx, fill=self.fill, expand=self.expand)


class Frame:

    def __init__(self, items = [], bg="Black", expand=tk.NO,side= None) -> None:
        
        self.items = items
        self.bg = bg
        self.expand = expand
        self.side = side
  

    def __str__(self) -> str:
        pass

    def pack(self, master):

        Frame = tk.Frame(master, bg= self.bg)
        
        for element in self.items:
            element.pack(Frame)

        Frame.pack(expand=self.expand,side=self.side)



class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Système de Changement de Page")

        # Dictionnaire pour stocker les différentes pages
        self.pages = {}

        # Création des pages
        page1 = Page1(self)
        page2 = Page2(self)

        # Ajout des pages au dictionnaire
        self.pages["Page1"] = page1
        self.pages["Page2"] = page2

        # Afficher la première page
        self.show_page("Page1")

    def show_page(self, page_name):
        # Afficher la page spécifiée
        page = self.pages[page_name]
        page.tkraise()

class Page1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Page 1")
        label.pack(padx=10, pady=10)

        # Ajouter les éléments spécifiques à la Page 1

        button = tk.Button(self, text="Aller à la Page 2", command=lambda: master.show_page("Page2"))
        button.pack(pady=10)

class Page2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Page 2")
        label.pack(padx=10, pady=10)

        # Ajouter les éléments spécifiques à la Page 2

        button = tk.Button(self, text="Retour à la Page 1", command=lambda: master.show_page("Page1"))
        button.pack(pady=10)

if __name__ == "__main__":
    app = Application()
    app.geometry("400x300")
    app.mainloop()