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
dot_cmds = ['all', 'count', 'show', 'destroy', 'update']


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


    def do_show(self, args):
        """Usage: show <class> <id> or <class>.show(<id>)\n     
        Display the string representation of a class instance of
        a given id.
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_id = args[1]
        all_instances = models.storage.all()
        found = False
        for key, instance in all_instances.items():
            if class_name in key and class_id in key:
                found = True
                print(instance)
                break
        if not found:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
