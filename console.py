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
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        """empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit the program
        """
        return True

    def do_create(self, classname=None):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not classname:
            print('** class name missing **')
        elif not self.classes.get(classname):
            print('** class doesn\'t exist **')
        else:
            obj = self.clslist[classname]()
            models.storage.save()
            print(obj.id)

    def do_destroy(self, arg):
        """destroy instance based on id
        """
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
            k = classname + "." + obj_id
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[k]
                models.storage.save()

    def do_all(self, arg):
        """Prints all instances based or not on the class name
        """
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            if not self.clslist.get(arg):
                print("** class doesn't exist **")
                return False
            print([str(v) for k, v in models.storage.all().items()
                   if type(v) is self.clslist.get(arg)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        classname, obj_id, atrr_name, attr_val = None, None, None, None
        updatetime = datetime.now()
        args = arg.split(' ', 3)
        if len(args) > 0:
            classname = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if len(args) > 2:
            atrr_name = args[2]
        if len(args) > 3:
            attr_val = list(shlex(args[3]))[0].strip('"')
        if not classname:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not atrr_name:
            print('** attribute name missing **')
        elif not attr_val:
            print('** value missing **')
        elif not self.clslist.get(classname):
            print("** class doesn't exist **")
        else:
            k = classname + "." + obj_id
            obj = models.storage.all().get(k)
            if not obj:
                print('** no instance found **')
            else:
                if hasattr(obj, atrr_name):
                    attr_val = type(getattr(obj, atrr_name))(attr_val)
                else:
                    attr_val = self.getType(attr_val)(attr_val)
                setattr(obj, atrr_name, attr_val)
                obj.updated_at = updatetime
                models.storage.save()

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
            print("**no instance found**")

    def do_destroy(self, args):
        """
        Usage: destroy <class> <id> or <class>.destroy(<id>)
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
        found = False
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()
        instance = all_instances.pop(key)
        if instance:
            del instance
            models.storage.save()
            found = True
        if not found:
            print("**no instance found**")

    def do_all(self, args):
        """
        Usage: all or all <class> or <class>.all()
        """
        args = args.split()
        class_name = args[0]
        if class_name:
            if class_name not in classes:
                print("** class doesn't exist **")
                return
        else:
            all_instances = models.storage.all()
            for key, instance in all_instances.items():
                print([str(instance)])

    def do_update(self, args, attribute_name=None, attribute_value=None):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = args.split()
        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        found = False
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()

        for key, instance in all_instances.items():
            if instance_id in key:
                found = True
                if len(args) < 5:
                    setattr(instance, attribute_name,
                            attribute_value.strip('"'))
                    models.storage.save()

        if not found:
            print("** no instance found **")

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]

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
