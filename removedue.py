
#import webbrowser
from tkinter import Button, Label,Entry,Tk
import os
import datetime
#import shutil
from tkinter import messagebox as msg
from tkinter import simpledialog as sd

def rndm():
	return str(datetime.datetime.now()).replace(" ","").replace("-","").replace(".","").replace(":","")



def removeDue():
	w=sd.askstring("Remove due","Enter id of member")
	if (w in os.listdir("members")):
		book_id=open("members/"+w+"/book","r").read().split("\n")[1]
		open("books/"+book_id+"/available","w").write("0")
		open("members/"+w+"/book","w").write("0")
		msg.showinfo("Remove due","Due removed successfully.")
	else:
		msg.showerror("Error","Member not found")