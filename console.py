#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines HBNBCommand class
    that implements the console
    for the AirBnB clone web application
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to quit the program"""
        return True

    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
