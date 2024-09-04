from tkinter import *
from tkinter import ttk
 
def boton():
    txt.set("El boton fue presionado")
root = Tk()
root.title("Boton")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

txt = StringVar()
ttk.Label(mainframe, textvariable=txt).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Mensaje", command=boton).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", boton)

root.mainloop()