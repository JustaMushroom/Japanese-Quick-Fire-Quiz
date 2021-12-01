import tkinter as tk
from tkinter import Tk, ttk, messagebox
from functools import partial

rootMenu = Tk()
rootKanaTest = Tk()
rootKanaTest.withdraw()

tests = ["Hiragana Test", "Katakana Test", "Mixed Test"]
testButtons = []

def on_close():
	if messagebox.askokcancel("Exit", "Do you want to quit?"):
		rootMenu.destroy()
		rootKanaTest.destroy()

rootMenu.protocol("WM_DELETE_WINDOW", on_close)

rootKanaTest.protocol("WM_DELETE_WINDOW", on_close)
rootKanaTest.bind("<Return>", answer)

def button_click(testType):
    messagebox.showinfo("Info", testType)

for test in tests:
    testID = tests.index(test)
    button = ttk.Button(text=test, command=lambda x=testId: button_click(x)).pack()

rootMenu.mainloop()