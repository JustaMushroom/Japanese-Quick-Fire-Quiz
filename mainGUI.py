import tkinter as tk
from tkinter import Tk, ttk, messagebox
from functools import partial
from testInfo import kana_hiragana, kana_katakana
from random import randint

score = 0

rootMenu = Tk()
rootMenu.geometry("400x200")
rootMenu.title("Main menu")
rootKanaTest = Tk()
rootKanaTest.withdraw()
rootKanaTest.geometry("400x200")

tk.Label(rootMenu, text="Please Choose a test to Continue").pack()

question = tk.Label(rootKanaTest, text="Question Here", font=("Arial", 25))
question.pack()

inputBox = tk.Entry(rootKanaTest, exportselection=0)
inputBox.pack()

tests = ["Hiragana Test", "Katakana Test", "Mixed Test"]
testButtons = []

def on_close():
	if messagebox.askokcancel("Exit", "Do you want to quit?"):
		rootMenu.destroy()
		rootKanaTest.destroy()

def on_close_test():
	if messagebox.askokcancel("Exit", "Do you want to exit the test?"):
		end_test()

rootMenu.protocol("WM_DELETE_WINDOW", on_close)

rootKanaTest.protocol("WM_DELETE_WINDOW", on_close_test)

def start_test(testType):
    rootKanaTest.title(tests[testType])
    rootMenu.withdraw()
    rootKanaTest.deiconify()
    updateTest()

def end_test():
    rootKanaTest.withdraw()
    rootMenu.deiconify()

def button_click(test_type):
    global testType
    testType = test_type
    start_test(testType)

def checkAnswer(event):
    answer = inputBox.get()
    global correctAnswer
    global score

    if answer.upper() == correctAnswer:
        score += 1
        messagebox.showinfo("Answer", "Correct Answer\nScore: {}".format(score))
        updateTest()
        inputBox.delete(0, "end")
    elif answer.upper() != correctAnswer:
        messagebox.showerror("Answer", "Incorrect Answer\nYour Score was {}".format(score))
        end_test()

def updateTest():
    hiragana = tuple(kana_hiragana)
    katakana = tuple(kana_katakana)
    global testType
    global correctAnswer
    global score
    if testType == 0:
        id = randint(0, len(hiragana)-1)
        correctAnswer = hiragana[id].upper()
        question.config(text=kana_hiragana[hiragana[id]])
    elif testType == 1:
        id = randint(0, len(katakana)-1)
        correctAnswer = katakana[id].upper()
        question.config(text=kana_katakana[katakana[id]])
    elif testType == 2:
        kh = randint(0, 100) % 2
        if kh == 0:
            id = randint(0, len(hiragana)-1)
            correctAnswer = hiragana[id].upper()
            question.config(text=kana_hiragana[hiragana[id]])
        elif kh == 1:
            id = randint(0, len(katakana)-1)
            correctAnswer = katakana[id].upper()
            question.config(text=kana_katakana[katakana[id]])
    
    rootKanaTest.focus_force()
    inputBox.focus()




for test in tests:
    testID = tests.index(test)
    button = ttk.Button(text=test, command=lambda x=testID: button_click(x)).pack()


rootKanaTest.bind("<Return>", checkAnswer)

rootMenu.mainloop()