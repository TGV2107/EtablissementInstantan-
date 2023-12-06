import tkinter as TK


class Label:

    def __init__(self, text : str, font : tuple = ("Helvetica", 35), bg : str = "Black", pady : int = 0, padx : int = 0, fill = None, expand = TK.NO) -> None:
        
        self.text = text
        self.font = font
        self. bg = bg
        self.pady = pady
        self.padx = padx
        self.fill = fill
        self.expand = expand

    def __str__(self) -> str:
        pass

    def pack(self, master):

        label = TK.Label(master, text=self.text, font=self.font, bg=self.bg)
        label.pack(pady=self.pady, padx=self.padx, fill=self.fill, expand=self.expand)

class Frame:

    def __init__(self, items = [], bg="Black",expand=TK.NO) -> None:
        
        self.items = items

        self.bg = bg
        self.expand = expand

    def __str__(self) -> str:
        pass

    def pack(self, master):

        Frame = TK.Frame(master, bg= self.bg)
        
        for element in self.items:
            element.pack(Frame)

        Frame.pack(expand=self.expand)
        
