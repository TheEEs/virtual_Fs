from imaplib import Commands
from system.machine import my_machine
from components import *
import re

NAME = "[\w\.\/]"

def take_input():
        r = []
        seq = input()
        i = 0
        l = len(seq)
        while i < l:
            if re.search(NAME, seq[i]):
                i, t = scan_text(seq, i)
                r.append(t)
            elif seq[i] == "-":
                i, t = scan_option(seq, i)
                r.append(t)
            elif seq[i] == '"':
                i, t = scan_quote(seq, i)
                r.append(t)
            else:
                raise SyntaxError()
            i += 1
        return r


def scan_text(seq: str, i: int):
    l = len(seq)
    r = seq[i]
    i += 1
    while i < l:
        if re.search(NAME, seq[i]):
            r = f"{r}{seq[i]}"
        else:
            break
        i += 1
    return i, r


def scan_option(seq: str, i: int):
    l = len(seq)
    i += 1
    while seq[i] == "-":  # skip all the dash "-"
        i += 1
    r = ""
    while i < l:
        if re.search(NAME, seq[i]):
            r = f"{r}{seq[i]}"
        else:
            break
        i += 1
    return i, f"-{r}"


def scan_quote(seq: str, i: int):
    i += 1
    l = len(seq)
    r = ""
    while i < l:
        if seq[i] != '"':
            r = f"{r}{seq[i]}"
        else:
            break
        i += 1
    return i, r

from system.commands import Commands

class REPL(Commands):
    def run_shell(self):
        self.terminate = False
        while not self.terminate:
            fs = my_machine.file_system
            usr = my_machine.current_user
            fs.rootfs.add_file("x")
            fs.rootfs.add_file("a")
            fs.rootfs.add_file("b")
            fs.rootfs.add_file("c")
            fs.rootfs.add_dir("folder1").add_dir("folder2")
            cwd = fs.current_working_directory.full_path()
            print(f"{usr.name}@{(cwd or '/')}: ", end="")
            user_input = take_input()
            self.__getattribute__(user_input[0])(my_machine,user_input[1:])
    


REPL().run_shell()
