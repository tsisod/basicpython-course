from platform import python_branch
from tkinter import*
from tkinter import ttk
import webbrowser
import pyautogui as pg
import time
GUI =Tk()
GUI.title('GUI.py')
GUI.geometry('500x400')


def Calendar():
    pg.click(994,12)

def youtube():
    webbrowser.open('https://youtu.be/7tZhvuZ4Q58')

def facebook(): # Open Python Video on Facebook
    webbrowser.open('https://www.facebook.com')
    time.sleep(2.3)
    pg.click(2032,925) #click Python for Beginners
    time.sleep(10)
    pg.scroll(-2)
    time.sleep(2.3)
    pg.click(2906,736)
    time.sleep(5)
    time.sleep(2)
    pg.click(2558,820)
    time.sleep(5.4)
    pg.scroll(-4)
    time.sleep(1.9)
    pg.click(2620,583)
    time.sleep(1.9)
    pg.click(2807,870)


def Calculator():
    pg.click(30,827)

B1 = Button(GUI,text='calendar',command=Calendar)
B1.pack(ipadx=20, ipady=10, pady=20)

B2 = ttk.Button(GUI,text='youtube',command=youtube)
B2.pack(ipadx=20, ipady=10, pady=20)

B3 = ttk.Button(GUI,text='Python by Uncle Engineer',command=facebook)
B3.pack(ipadx=20, ipady=10, pady=20)

B4 = ttk.Button(GUI,text='Calculator',command=Calculator)
B4.pack(ipadx=20, ipady=10, pady=20)

GUI.mainloop() 