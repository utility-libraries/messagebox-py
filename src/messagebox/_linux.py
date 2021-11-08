# -*- coding=utf-8 -*-
r"""
possible option is /usr/bin/notify-send
"""
import subprocess


MB_INFO = '--info'
MB_WARNING = '--warning'
MB_ERROR = '--error'
MB_QUESTION = '--question'


def _msg(title: str, message: str, what):
    result = subprocess.run([
        '/usr/bin/zenity',
        what,
        '--title', title,
        '--text', message
    ])
    return result.returncode


def showinfo(title: str, message: str):
    _msg(title, message, MB_INFO)


def showwarning(title: str, message: str):
    _msg(title, message, MB_WARNING)


def showerror(title: str, message: str):
    _msg(title, message, MB_ERROR)


def askquestion(title: str, message: str):
    print(_msg(title, message, MB_QUESTION))


def askokcancel(title: str, message: str):
    pass


def askyesno(title: str, message: str):
    _msg(title, message, MB_INFO)


def askyesnocancel(title: str, message: str):
    pass


def askretrycancel(title: str, message: str):
    pass
