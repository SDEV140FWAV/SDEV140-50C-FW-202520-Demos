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
        self.bind("<Button-1>", self.mouse_pressed)
        self.bind("<B1-Motion>", self.mouse_dragged)
        self.bind("<ButtonRelease-1>", self.mouse_released)
    
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

    def mouse_pressed(self, event):
        x = event.x_root - self.master.winfo_rootx()
        y = event.y_root - self.master.winfo_rooty()
        self.master.event_generate("<Button-1>", x=x, y=y)
    
    def mouse_dragged(self,event):
        x = event.x_root - self.master.winfo_rootx()
        y = event.y_root - self.master.winfo_rooty()
        self.master.event_generate("<B1-Motion>", x=x, y=y)
    
    def mouse_released(self,event):
        x = event.x_root - self.master.winfo_rootx()
        y = event.y_root - self.master.winfo_rooty()
        self.master.event_generate("<ButtonRelease-1>", x=x, y=y)

class GameArea(tk.Canvas):
    def __init__(self, master):
        super().__init__(master,background="green")
        self.pack(fill="both", expand=True)
        self.game = Game()
        self.foundation_pos = [{"x":150, "y":100},{"x":275, "y":100},{"x":400, "y":100}, {"x":525,"y":100}]
        self.waste_pos = [{"x":150, "y":275},{"x":275, "y":275},{"x":400, "y":275}, {"x":525,"y":275}]
        self.draw_card_pos = {"x":450, "y":500 }
        for i in range(4):
            foundation = CardRender(self,self.game.foundations[i].viewTopCard())
            self.create_window(self.foundation_pos[i]["x"], self.foundation_pos[i]["y"],window=foundation)
            self.create_rectangle(self.waste_pos[i]["x"]-50, self.waste_pos[i]["y"]-75,self.waste_pos[i]["x"] + 50, self.waste_pos[i]["y"] + 75, fill="white",width="2")
        self.drawn_card = None
        self.selected_item = None
        self.waste_num = -1
        self.waste_card = [0,0,0,0]
        self.create_rectangle(self.draw_card_pos["x"] - 50, self.draw_card_pos["y"] - 75, self.draw_card_pos["x"] + 50, self.draw_card_pos["y"] + 75, fill="white", width=2)
        self.create_window(275,500, window=CardRender(self,None))
        self.draw_button = tk.Button(self.master, text="Draw Card", command=self.draw_card)
        self.create_window(150, 500, window=self.draw_button)
        self.bind("<Button-1>", self.mouse_pressed)
        self.bind("<B1-Motion>", self.mouse_dragged)
        self.bind("<ButtonRelease-1>", self.mouse_released)

    def draw_card(self):
        self.game.drawCard()
        self.drawn_card = CardRender(self, self.game.card_to_play)
        self.drawn_card = self.create_window(self.draw_card_pos["x"], self.draw_card_pos["y"], window = self.drawn_card)
        self.draw_button.configure(state="disabled")

    def mouse_pressed(self, event):
        self.x = event.x
        self.y = event.y
        self.selected_item = self.find_clicked_item(self.x, self.y)
        if self.selected_item == None and self.waste_num != -1:
            self.selected_item = self.waste_card[self.waste_num]
        elif self.selected_item != None:
            print(self.game.card_to_play)

    def mouse_dragged(self, event):
        if self.selected_item:
            xDistance = event.x - self.x
            yDistance = event.y - self.y
            self.move(self.selected_item, xDistance, yDistance)
            self.x = event.x
            self.y = event.y

    
    def mouse_released(self,event):
        if self.selected_item == None:
            return
        
        foundationDrop = self.find_foundation(event.x, event.y)
        if foundationDrop != None:
            try:
                if self.waste_num != -1:
                    self.game.playWasteCard(self.waste_num, foundationDrop)
                    
                    if len(self.game.wastes[self.waste_num]) > 0:
                        self.waste_card[self.waste_num] = self.create_window(self.waste_pos[self.waste_num]["x"], self.waste_pos[self.waste_num]["y"], window=CardRender(self, self.game.wastes[self.waste_num].viewTopCard()))
                    else:
                        self.waste_card[self.waste_num] = 0
                    self.waste_num = -1
                else:
                    self.game.playDrawnCard(foundationDrop)
                    self.drawn_card = 0
                
                self.delete(self.selected_item)
                self.selected_item = None
                card = CardRender(self, self.game.foundations[foundationDrop].viewTopCard())
                
                self.create_window(self.foundation_pos[foundationDrop]["x"], self.foundation_pos[foundationDrop]["y"], window=card)
                for i in range(4):
                    if self.waste_card[i] != 0:
                        self.delete(self.waste_card[i])
                        self.waste_card[i] = self.create_window(self.waste_pos[i]["x"], self.waste_pos[i]["y"], window=CardRender(self, self.game.wastes[i].viewTopCard()))
            except:
                 if self.waste_num != -1:
                     x = self.waste_pos[self.waste_num]["x"] - self.coords(self.selected_item)[0]
                     y = self.waste_pos[self.waste_num]["y"] - self.coords(self.selected_item)[1]
                     self.move(self.selected_item, x,y)
                 else:
                     x = self.draw_card_pos["x"] - self.coords(self.selected_item)[0] 
                     y = self.draw_card_pos["y"] - self.coords(self.selected_item)[1] 
                     self.move(self.selected_item, x, y)

                 self.waste_num = -1
                 self.selected_item = None
        elif self.waste_num != -1:
            x = self.waste_pos[self.waste_num]["x"] - self.coords(self.selected_item)[0]
            y = self.waste_pos[self.waste_num]["y"] - self.coords(self.selected_item)[1]
            self.move(self.selected_item, x, y)

        else:
            wasteDrop = self.find_waste(event.x, event.y)
            if wasteDrop != None:
                self.game.playDrawnCard(wasteDrop, "waste")
                self.delete(self.selected_item)
                self.selected_item = None
                self.waste_card[wasteDrop] = self.create_window(self.waste_pos[wasteDrop]["x"], self.waste_pos[wasteDrop]["y"], window=CardRender(self, self.game.wastes[wasteDrop].viewTopCard()))
                self.drawn_card = 0
            else:
                x = self.draw_card_pos["x"] - self.coords(self.selected_item)[0] 
                y = self.draw_card_pos["y"] - self.coords(self.selected_item)[1] 
                self.move(self.selected_item, x, y)
        if self.game.card_to_play == None:
            self.draw_button.configure(state="normal")



    
    def find_clicked_item(self, x, y):
        if self.game.card_to_play != None:
            coords = [self.draw_card_pos["x"] -50, self.draw_card_pos["y"]-75, self.draw_card_pos["x"]+50, self.draw_card_pos["y"]+75]
            if self.contains_point(coords, x, y):
                return self.drawn_card
        for i in range(4):
            if len(self.game.wastes[i]) != 0:
                coords = [self.waste_pos[i]["x"] - 50, self.waste_pos[i]["y"] - 75, self.waste_pos[i]["x"] + 50, self.waste_pos[i]["y"] + 75]
                if self.contains_point(coords, x, y):
                    self.waste_num = i
                    return self.waste_card[i]
        self.waste_num = -1
        return None
            
    def contains_point(self, coords, x, y):
        return x >= min(coords[0], coords[2]) and x <= max(coords[0], coords[2]) and y >= min(coords[1],coords[3]) and y <= max(coords[1], coords[3])
    
    def find_foundation(self, x, y):
        for i in range(4):
            coords = [self.foundation_pos[i]["x"] - 50, self.foundation_pos[i]["y"] - 75, self.foundation_pos[i]["x"] + 100, self.foundation_pos[i]["y"] + 150]
            if self.contains_point(coords, x, y):
                return i
        return None
    
    def find_waste(self, x, y):
        for i in range(4):
            
            coords = [self.waste_pos[i]["x"] - 50, self.waste_pos[i]["y"] - 75, self.waste_pos[i]["x"] + 50, self.waste_pos[i]["y"] + 75]
            if self.contains_point(coords, x, y):
                
                return i
        return None   


if __name__ == "__main__":
    MainWindow().mainloop()
    