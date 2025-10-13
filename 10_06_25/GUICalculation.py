from game import Game
from card import Card
import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.geometry("800x600+300+300")
        self.master.title("Calculation")
        self.pack(fill="both", expand=True)
        self.gameArea = GameArea(self)
        


class CardRender(tk.Canvas):
    def __init__(self, master, card:Card):
        super().__init__(master, width=100, height=150, borderwidth=0, relief="flat", highlightthickness=0, background="white")
        self.card = card
        self.draw()
    
    def draw(self):
        if self.card == None:
            for i in range(0,151,24):
                for j in range(0, 101,24):
                    self.create_bitmap(j,i, bitmap="gray12", foreground="red")
        else:
            if self.card.suit == "DIAMONDS" or self.card.suit == "HEARTS":
                color = "red"
            else:
                color = "black"
            self.create_text(20,25, text=f"{self.card.rank}", fill=color,font=("TkDefaultFont",18))
            self.create_text(50,75, text=Card.SUIT_SYMBOL[self.card.suit], fill=color, font=("TkDefaultFont", 48))
            self.create_text(80,125,text=f"{self.card.rank}", fill=color,font=("courier",18))

class GameArea(tk.Canvas):
    def __init__(self, master):
        super().__init__(master,background="green")
        self.pack(fill="both", expand=True)
        self.game = Game()
        self.foundation_pos = [{"x":150, "y":100}]

        foundation = CardRender(self,self.game.foundations[0].viewTopCard())
        self.create_window(self.foundation_pos[0]["x"], self.foundation_pos[0]["y"],window=foundation)


if __name__ == "__main__":
    MainWindow().mainloop()
    