import math
import tkinter as tk
from random import randint
from threading import Thread, Event
from time import sleep
from tkinter import Tk, ttk, messagebox
from highscoreHandler import HighscoreHandler
from testInfo import kana_hiragana, kana_katakana

score = 0
timer = 0
timer_term = Event()
correctAnswer = ""
testType = ""

rootMenu = Tk()
rootMenu.geometry("400x200")
rootMenu.title("Main menu")
rootKanaTest = Tk()
rootKanaTest.withdraw()
rootKanaTest.geometry("400x200")

tk.Label(rootMenu, text="Please Choose a test to Continue").pack()

questionTitle = tk.Label(rootKanaTest, text="What is this character?")
questionTitle.pack()
question = tk.Label(rootKanaTest, text="Question Here", font=("Arial", 25))
question.pack()

inputBox = tk.Entry(rootKanaTest, exportselection=False)
inputBox.pack()

tests = ["Hiragana Test", "Katakana Test", "Mixed Test"]
testButtons = []

highscores = HighscoreHandler()

if len(highscores.contents) == 0:
    highscores.generateContents(tests, [int for x in tests])

def on_close():
    if messagebox.askokcancel("Exit", "Do you want to quit?"):
        rootMenu.destroy()
        rootKanaTest.destroy()


def on_close_test():
    if messagebox.askokcancel("Exit", "Do you want to exit the test?"):
        end_test()


def timer_increment(term_event_in: Event):
    global timer
    while True:
        sleep(0.01)
        timer += 0.01

        if term_event_in.is_set():
            term_event_in.clear()
            return

def showHighscores():
    highscorestr = highscores.getScoreString()

    messagebox.showinfo("High Scores", "Here are the high scores\n" + highscorestr)


rootMenu.protocol("WM_DELETE_WINDOW", on_close)

rootKanaTest.protocol("WM_DELETE_WINDOW", on_close_test)


def start_test(testType):
    global timer
    global score
    score = 0
    timer = 0
    timerThread: Thread = Thread(target=timer_increment, args=(timer_term,))
    rootKanaTest.title(tests[testType])
    rootMenu.withdraw()
    rootKanaTest.deiconify()
    updateTest()
    timerThread.start()


def end_test():
    rootKanaTest.withdraw()
    rootMenu.deiconify()
    timer_term.set()


def button_click(test_type):
    global testType
    testType = test_type
    start_test(testType)


def checkAnswer(event):
    answer = inputBox.get()
    global correctAnswer
    global score
    global timer

    if answer.upper() == correctAnswer:
        score += 1
        messagebox.showinfo("Answer", "Correct Answer\nScore: {}".format(score))
        try:
            updateTest()
        except RecursionError:
            return
    elif answer.upper() != correctAnswer:
        timeMinutes = math.floor(timer / 60)
        timeSeconds = round(timer - (timeMinutes * 60), 2)
        messagebox.showerror("Answer",
                             "Incorrect Answer, the answer was actually \"{}\"\nYour Score was {:,}\nYour time was {} "
                             "minutes and {} seconds".format(
                                 correctAnswer.lower(), score, timeMinutes, timeSeconds))
        if score > highscores.contents[tests[testType]]:
            messagebox.showinfo("High Score!", "New High Score! Previous Highscore was {:,}.".format(highscores.getScores()[tests[testType]]))
            highscores.updateScore(tests[testType], score)
            highscores.saveHighScores()
        end_test()


def updateTest():
    hiragana = tuple(kana_hiragana)
    katakana = tuple(kana_katakana)
    global testType
    global correctAnswer
    global score
    if testType == 0:
        id = randint(0, len(hiragana) - 1)
        correctAnswer = hiragana[id].upper()
        questionTitle.config(text="What is this Hiragana Character?")
        question.config(text=kana_hiragana[hiragana[id]])
    elif testType == 1:
        id = randint(0, len(katakana) - 1)
        correctAnswer = katakana[id].upper()
        questionTitle.config(text="What is this Katakana Character?")
        question.config(text=kana_katakana[katakana[id]])
    elif testType == 2:
        kh = randint(0, 100) % 2
        if kh == 0:
            id = randint(0, len(hiragana) - 1)
            correctAnswer = hiragana[id].upper()
            questionTitle.config(text="What is this Hiragana Character?")
            question.config(text=kana_hiragana[hiragana[id]])
        elif kh == 1:
            id = randint(0, len(katakana) - 1)
            correctAnswer = katakana[id].upper()
            questionTitle.config(text="What is this Katakana Character?")
            question.config(text=kana_katakana[katakana[id]])

    inputBox.delete(0, "end")
    rootKanaTest.focus_force()
    inputBox.focus()


for test in tests:
    testID = tests.index(test)
    ttk.Button(text=test, command=lambda x=testID: button_click(x)).pack()

ttk.Button(rootMenu, text="Show Highscores", command=showHighscores).pack()

rootKanaTest.bind("<Return>", checkAnswer)

rootMenu.mainloop()
