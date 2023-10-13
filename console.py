#!/usr/bin/env python
"""Method Command Interpreter"""
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    }


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    
    def do_quit(self, args):
        '''<Quit> Command To Exit The Program'''
        return True

    def do_EOF(self, args):
        '''Handles end of file'''
        print()
        return True

    def emptyline(self):
        '''dont execute anything when user
           press enter an empty line
        '''
        pass

    def do_help(self, args):
        """display help informaiton about the commands"""
        cmd.Cmd.do_help(self, args)

    def do_create(self, args):
        """
        Usage: create<class>\n
        Create a new class instance and print its id
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
