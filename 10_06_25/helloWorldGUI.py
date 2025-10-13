import tkinter as tk

root = tk.Tk()
btn1 = tk.Button(root,text="Hello World!")
btn1.grid(row = 0, column= 0)
btn2 = tk.Button(root, text="Hello World2!")
btn2.grid(row = 0, column= 1)
btn3 = tk.Button(root, text="Hello World3!")
btn3.grid(row = 1, column= 0, columnspan=2, sticky="nsew")
btn4 = tk.Button(root, text="Hello World4!")
btn4.grid(row = 0, column= 2, rowspan=2, sticky="ns")

root.title("Hello World!")
root.geometry("640x480+300+300")
root.resizable(False, False)




root.mainloop()