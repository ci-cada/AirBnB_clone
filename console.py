#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from datetime import datetime
from shlex import shlex

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

class HBNBCommand(cmd.Cmd):
    """ hbnb shell """
    prompt = '(hbnb) '
    
    def emptyline(self):
        """empty line"""
        pass

    def do_show(self, arg):
        """Show instance based on id"""
        classname, obj_id = None, None
        args = arg.split(' ')
        if len(args) > 0:
            classname = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not classname:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not self.classes.get(classname):
            print("** class doesn't exist **")
        else:
            item = classname + "." + obj_id
            obj = models.storage.all().get(item)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit the program
        """
        return True

    def default(self, line):
        """ class command handler """
        ln = line.split('.', 1)
        if len(ln) < 2:
            print('*** Unknown syntax:', ln[0])
            return False
        classname, line = ln[0], ln[1]
        if classname not in list(self.classes.keys()):
            print('*** Unknown syntax: {}.{}'.format(classname, line))
            return False
        ln = line.split('(', 1)
        if len(ln) < 2:
            print('*** Unknown syntax: {}.{}'.format(classname, ln[0]))
            return False
        method_name, args = ln[0], ln[1].rstrip(')')
        if method_name not in ['all', 'count', 'show', 'destroy', 'update']:
            print('*** Unknown syntax: {}.{}'.format(classname, line))
            return False
        if method_name == 'all':
            self.do_all(classname)
        elif method_name == 'count':
            print(self.count_class(classname))
        elif method_name == 'show':
            self.do_show(classname + " " + args.strip('"'))
        elif method_name == 'destroy':
            self.do_destroy(classname + " " + args.strip('"'))
        elif method_name == 'update':
            curly_l, curly_r = args.find('{'), args.find('}')
            check = None
            if args[curly_l:curly_r + 1] != '':
                check = eval(args[curly_l:curly_r + 1])
            ln = args.split(',', 1)
            obj_id, args = ln[0].strip('"'), ln[1]
            if check and type(check) is dict:
                self.handle_dict(classname, obj_id, check)
            else:
                from shlex import shlex
                args = args.replace(',', ' ', 1)
                ln = list(shlex(args))
                ln[0] = ln[0].strip('"')
                self.do_update(" ".join([classname, obj_id, ln[0], ln[1]]))

    def handle_dict(self, classname, obj_id, _dict):
        """handle dictionary update"""
        for key, value in _dict.items():
            self.do_update(" ".join([classname, obj_id, str(key), str(value)]))

    def postloop(self):
        """print new line after each loop"""
        print()

    def do_create(self, args):
        """
        Usage: create <class>
        Creates a new instance of BaseModel, and prints the id
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

    def do_show(self, args):
        """
        Usage: show <class> <id> or <class>.show(<id>)
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
                print("**no instance found")



    @staticmethod
    def count_class(classname):
        """count number of objects of type class name"""
        counter = 0
        for key, value in models.storage.all().items():
            if type(value).__name__ == classname:
                counter += 1
        return counter


if __name__ == "__main__":
    HBNBCommand().cmdloop()
