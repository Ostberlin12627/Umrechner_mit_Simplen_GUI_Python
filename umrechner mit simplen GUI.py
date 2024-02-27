from tkinter import *
from tkinter import font
ascii = []

root = Tk()
root.title("Umrechner")
font_general = font.Font(size=14, family="Arial")

def werte_zum_umrechnen():
    dezimalzahl = int(zahl.get())
    basis = int(basiseingabe.get())
    ende = str(dezimal_zu_anderer_basis(dezimalzahl, basis))
    ausgabe.configure(text=ende)
    zahl.delete(0, END)
    basiseingabe.delete(0, END)

def entfernen():
    ausgabe.configure(text="", font=font_general)
    ausgabe.grid(row=3, column=0)

def dezimal_zu_anderer_basis(dezimalzahl,basis):
    while dezimalzahl >0:
        rechnung = int(((dezimalzahl / basis) - int(dezimalzahl / basis)) * basis)
        #              (     (35 / 2)         -     (34 /2)     )         *   2
        if rechnung >10:
            ascii.append(chr(rechnung + 55))
        else:
            ascii.append(str(rechnung))
        dezimalzahl = int(dezimalzahl / basis)
    ascii.reverse()
    ergebnis = "".join(ascii)
    return ergebnis

zahl = Entry(root,font=font_general)
zahl.grid(row=0, column=1, sticky="nswe")
basiseingabe = Entry(root,font=font_general)
text = Label(root,text="Dezimalzahl",font=font_general)
text.grid(row=0,column=0, sticky="nswe")
text1 = Label(root,text="Basis",font=font_general)
text1.grid(row=1,column=0, sticky="nswe")
basiseingabe.grid(row=1, column=1, sticky="nswe")
ok_button = Button(root,relief="raised",text= "OK", command=werte_zum_umrechnen,font=font_general)
ok_button.grid(row=2, column = 0)
loeschen_button = Button(root,relief="raised",text= "Löschen",command=entfernen,font=font_general)
loeschen_button.grid(row=2, column = 1)
ausgabe = Label(root, text="Hier wird das Ergebnis stehen",font=font_general,)
ausgabe.grid(row=3,column=0)

for column in range(4):
    root.columnconfigure(column, weight=1)
for row in range(3):
    root.rowconfigure(row, weight=1)

root.mainloop()