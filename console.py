#!/usr/bin/python3
"""Defines entry point of the command interpreter"""

import cmd

class_dict = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """Defines HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to quit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in class_dict:
            print("** class doesn't exist **")
            return

        new_obj = class_dict[arg]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        obj_dict = storage.all()
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
            return
        inst = "{}.{}".format(args[0], args[1])
        if inst not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[inst])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        obj_dict = storage.all()
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in class_dict:
            print("** class doesn't exist **")
            return
        if args == 1:
            print("** instance id missing **")
            return
        inst = "{}.{}".format(args[0], args[1])
        if inst not obj_dict:
            print("** no instance found **")
            return
        del obj_dict[inst]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """


    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
