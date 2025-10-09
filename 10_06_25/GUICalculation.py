from game import Game
import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.geometry("800x600+1900+300")
        self.master.title("Calculation")
        self.pack(fill="both", expand=True)

if __name__ == "__main__":
    MainWindow().mainloop
    