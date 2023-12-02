class Window:
    def __init__(self,name,size) -> None:
        self.name = name
        self.size = size
        

    def __str__(self) -> str:
        return (self.name + "De taille " + self.size)

    def display(self):
        pass
