from tkinter import messagebox
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter import ttk
from tkinter.filedialog import askdirectory
from editor import Renamer

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb 

def click_rename_button():
    if input_name.get() != '' and dirselector["text"] != 'Открыть':
        print('renaming ' + input_name.get() + " " + directory)
        project = Renamer(directory.replace('/','\\'), input_name.get())
        project.start()
        messagebox.showinfo(title=None, message=project.printCatalog())
    else:
        messagebox.showerror(title=None, message="Что-то не так, заполните все поля")

def click_button():
    global directory
    directory = askdirectory()
    dirselector["text"] = directory.split('/')[-1]

    
root = Tk()
root.geometry('300x165')
root.title('justacold\'s renamer')
root.config(background=rgb_hack((30, 30, 30)))

ttk.Label(text="Выберите папку (клик на кнопку)", background=rgb_hack((30, 30, 30)), foreground=rgb_hack((255,255,255))).pack(pady=(10,0))
directory = "Открыть"
dirselector = ttk.Button(text=directory, command=click_button) # show an "Open" dialog box and return the path to the selected file
dirselector.pack()

ttk.Label(text="Новое имя ", background=rgb_hack((30, 30, 30)), foreground=rgb_hack((255,255,255))).pack(pady=(10,0))

input_name = ttk.Entry()
input_name.pack()

submit = ttk.Button(text="Переименовать проект", command=click_rename_button)
submit.pack(pady=(15, 3))

root.mainloop()