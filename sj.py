from tkinter import *
from tkinter.messagebox import showinfo

'''Program to rename multiple files in a single folder with common naming system and incrementing number at the end'''
import os

window = Tk()
def chnge():
    i = 1
    path = str(loc_e.get()) #set path = the path of the folder where you want to do the renaming task. Make sure its in the single quotes
    stname = str(nam_e.get())#set stname = the common characters/name you want for the files which wont change in every files of that folder
    exten = str(ext_e.get())#set exten = the extension of file you want to have.
    try:

        #loop renaming the filenames
        for filename in os.listdir(path):
            dst = stname + str(i) + exten
            src = path + '/' + filename
            dst = path + '/' + dst
            os.rename(src, dst)
            i += 1

    except FileNotFoundError:
        showinfo("Error", "Enter Valid Location Dude!")

    except FileExistsError:
        showinfo("Error", "You High? this file already exists!")

    except OSError:
        showinfo("Error", "Will you plz Enter valid name with no special characters like \ / % * | and whatever... I dont know")

    else:
        showinfo("Success","Done Bruv (Sorry if you aren't.)! You owe me a cup of tea!!")

window.title("Naam Parivartan!")
window.iconbitmap(r'icon.ico')
name = Label(window, text="File Renaming tool v1.0.0.0.0.0", bg="orange").grid(row=0, columnspan=2, sticky=N)
location = Label(window, text="Enter the location").grid(row=1, column=0, sticky=E)
loc_e = Entry(window)
loc_e.grid(row=1, column=1, sticky=W)
nam_e = Entry(window)
nam_e.grid(row=2, column=1, sticky=W)
ext_e = Entry(window)
ext_e.grid(row=3, column=1, sticky=W)
com_name = Label(window, text="Enter the name").grid(row=2, column=0, sticky=E)
exten = Label(window, text="Enter the extension").grid(row=3, column=0, sticky=E)
submit = Button(window, command=chnge, text="Submit me", bg="#637985").grid(columnspan = 2)
quit = Button(window, command = window.quit, text = "Exit", bg="red").grid(columnspan = 2)

cred = Label(window, text="- Made By one and only Saurabh Jagtap").grid(columnspan = 2)
window.mainloop()
