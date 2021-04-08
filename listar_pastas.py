from tkinter import filedialog
from tkinter import *
from os import walk
#Jony bgud!
#Bezitos Carolinea

def browse_button():
    # Allow user to select a directory and store it in global var called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)
    return filename


root = Tk()
root.title("Listador da Carol")
root.minsize(640, 100)

folder_path = StringVar()
label = Label(master=root, textvariable=folder_path)
label.grid(column=3, row=1, padx=20, pady=20)
button = Button(text="Escolher diretório", command=browse_button)
button.grid(column=2, row=1)
f = []
my_path = browse_button()
for (dirpath, dirnames, filenames) in walk(my_path): #To be implemented a OptionMenu widget for choosing
    f.extend(dirnames)
    break
file = open('lista_diretorios.txt', 'w')  #Open or create a txt file to be written.
for i in f:
    file.write(i + '\n')
mainloop()
