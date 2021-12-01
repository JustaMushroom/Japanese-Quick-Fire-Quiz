import tkinter as tk
from tkinter import Tk, ttk, messagebox

rootKanaTest = Tk()
rootKanaTest.withdraw()

def on_close():
	if messagebox.askokcancel("Exit", "Do you want to quit?"):
		rootMenu.destroy()
		rootKanaTest.destroy()

        
