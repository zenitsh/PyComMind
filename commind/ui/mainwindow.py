#! /usr/bin/python3

import tkinter

class App(tkinter.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.config(width=1024,height=768)
        self.pack()

        self.entrythingy = tkinter.Entry()
        self.entrythingy.config(width=80)
        self.entrythingy.pack(side='bottom')

        self.contents = tkinter.StringVar()
        self.contents.set('this is a variable')

        self.entrythingy['textvariable'] = self.contents
        self.entrythingy.bind('<Key>',self.char)

        self.entrythingy.bind_all('<Control-;>',self.set_focus)

    def char(self,event):
        if event.char == '\r':
            print(self.contents.get())
            self.contents.set('')
        _text = self.contents.get()
        _text = _text.lstrip()
        self.contents.set(_text)
    
    def set_focus(self,event):
        self.contents.set('')
        self.entrythingy.focus()

def run():
    mainwindow = tkinter.Tk()
    mainwindow.title('PyComMind v1.0')
    App(mainwindow).mainloop()