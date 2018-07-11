#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""GUI for this tool"""

from tkinter import Tk, N, W, E, S, StringVar, filedialog, Text, VERTICAL, END
from tkinter import ttk
import os
import datetime


class App(object):

    def __init__(self):
        """Initial

        Create an app instance and do some basic settings.
        """

        # declare variable
        self._app = None
        self._mainframe = None
        self.dir_name = None
        self.out_name = None
        self.text = None

        # create app
        self.create_app()

        # create mainframe
        self.create_mainframe()

        # create input variable
        self.create_input_variable()

        # create and set input and output entries
        self.create_entries()

        # create and set perform button
        self.create_perform_button()

        # create and set log text box
        self.create_log_textbox()

    def start(self):
        """Run GUI

        :return: None
        """
        self._app.mainloop()

    def create_app(self):
        """Create application instance

        :return: None
        """
        app = Tk()
        app.title('Draw text into images')
        app.geometry('550x500')
        app.resizable(False, False)
        app.rowconfigure(0, weight=1)
        app.columnconfigure(0, weight=1)

        self._app = app

    def create_mainframe(self):
        """Create main frame

        :return: None
        """
        mainframe = ttk.Frame(self._app)
        mainframe['padding'] = (10, 10)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        # expand when windows resize
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self._mainframe = mainframe

    def create_input_variable(self):
        """Create and save input variables

        :return: None
        """
        self.dir_name = StringVar()
        self.out_name = StringVar()

    def create_entries(self):
        """Create two entries for receive user input

        Create two frames for layout, put label, entry and browse button inside it.

        :return: None
        """
        dir_input_frame = ttk.Frame(self._mainframe)
        dir_input_frame.grid(column=0, row=0, sticky=N)
        ttk.Entry(dir_input_frame, textvariable=self.dir_name, width=30).grid(column=1, row=0)
        ttk.Label(dir_input_frame, text='Input:', width=7).grid(column=0, row=0, sticky=E)
        ttk.Button(dir_input_frame, text='Browse',
                   command=lambda: self.ask_directory('dir_name')).grid(column=2, row=0)

        out_input_frame = ttk.Frame(self._mainframe, height=2)
        out_input_frame.grid(column=0, row=1, sticky=N)
        ttk.Entry(out_input_frame, textvariable=self.out_name, width=30).grid(column=1, row=0)
        ttk.Label(out_input_frame, text='Output:', width=7).grid(column=0, row=0, sticky=E)
        ttk.Button(out_input_frame, text='Browse',
                   command=lambda: self.ask_directory('out_name')).grid(column=2, row=0)

    def create_perform_button(self):
        """Create and bind handler to perform button

        :return: None
        """
        perform_frame = ttk.Frame(self._mainframe)
        perform_frame['padding'] = (10, 10)
        perform_frame.grid(column=0, row=2)
        perform = ttk.Button(perform_frame, text='Perform', command=self.perform_drawing)
        perform.grid(column=0, row=0)

    def create_log_textbox(self):
        """Create message box

        :return: None
        """
        text = Text(self._mainframe, height=25, border=None)
        text.grid(row=3, columnspan=3)
        scroll = ttk.Scrollbar(self._mainframe, orient=VERTICAL, command=text.yview)
        scroll.grid(column=1, row=3, sticky=(N, S))
        text.configure(yscrollcommand=scroll.set)
        text.insert('1.0', 'Select input and output directories, and click Perform button to start.\n')
        text['stat'] = 'disable'

        self.text = text

    def check_form(self):
        """Check if user input a valid data

        :return: True if ok else False
        """
        if not self.dir_name.get() or not self.out_name.get():
            self.insert_log('Input/Output is empty, check and try again please.')
            return False
        else:
            self.insert_log('Input: {}; Output: {}'.format(
                self.dir_name.get(),
                self.out_name.get()
            ))
            return True

    def perform_drawing(self):
        """Perform drawing

        :return: None
        """
        if not self.check_form():
            return
        self.insert_log('Mission started.')

    def insert_log(self, msg):
        """Insert logs into message box

        :param msg: message
        :return: None
        """
        text = self.text
        text['stat'] = 'normal'
        text.insert('end', '\n')
        text.insert('end', self.add_time_prefix(msg))
        text.see(END)
        text['stat'] = 'disable'

    def ask_directory(self, target):
        """Ask for select a directory

        :param target: which to store the result
        :return: None
        """
        p = filedialog.askdirectory()
        getattr(self, target).set(p)
        if p and target == 'dir_name' and not self.out_name.get():
            self.out_name.set(p + os.sep + 'out')

    @staticmethod
    def get_time():
        """Get formatted datetime

        :return: formatted datetime
        """
        return str(datetime.datetime.now())

    def add_time_prefix(self, msg):
        """Add timestamp prefix to specified message

        :param msg: message
        :return: result
        """
        return '{} {}'.format(
            self.get_time(),
            msg
        )


if __name__ == '__main__':
    a = App()
    a.start()
