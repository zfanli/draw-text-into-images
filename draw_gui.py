#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""GUI for this tool"""

from tkinter import Tk, N, W, E, S, StringVar
from tkinter import ttk


class App(object):

    def __init__(self):
        """Initial

        Create an app instance and do some basic settings.
        """
        app = Tk()
        app.title('Draw text into images')
        mainframe = ttk.Frame(app)
        mainframe['padding'] = (10, 10)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # expand when windows resize
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        dir_name = StringVar()
        ttk.Entry(app, textvariable=dir_name).grid(column=1, row=0)
        ttk.Label(mainframe, text='test').grid(column=6, row=99)

        self._app = app

    def start(self):
        self._app.mainloop()


if __name__ == '__main__':
    app = App()
    app.start()
