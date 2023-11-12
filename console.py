#!/usr/bin/python3
"""Console definition"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpreter """
    prompt = "(hbnb) "
    validClasses = ["BaseModel",
                    "User", "State",
                    "City", "Place",
                    "Review", "Amenity"]

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ exit from console with ctrl+d """
        print("")
        return True

    def emptyline(self):
        """ handle the empty line """
        pass

    def do_create(self, argument):
        """Creates a new instance """
        argz = argument.split()
        if len(argz) == 0:
            print("** class name missing **")
        elif argz[0] not in HBNBCommand.validClasses:
            print("** class doesn't exist **")
        else:
            objct = eval(argz[0])()
            objct.save()
            print(objct.id)

    def do_show(self, argument):
        """Use class name to print str representation of object"""
        argz = argument.split()
        obj_dictionary = storage.all()

        if len(argz) == 0:
            print("** class name missing **")
        elif argz[0] not in HBNBCommand.validClasses:
            print("** class doesn't exist **")
        elif len(argz) == 1:
            print("** instance id missing **")
        else:
            objct = "{}.{}".format(argz[0], argz[1])
            if objct not in obj_dictionary:
                print("** no instance found **")
            else:
                print(obj_dictionary[objct])

    def do_update(self, argument):
        """Updates/add attributes """
        argz = argument.split()
        if len(argz) == 0:
            print("** class name missing **")
            return
        cls_name = argz[0]
        if cls_name not in HBNBCommand.validClasses:
            print("** class doesn't exist **")
            return

        if len(argz) < 2:
            print("** instance id missing **")
            return
        objct_id = argz[1]
        obj_dictionary = storage.all()
        objct_key = "{}.{}".format(cls_name, objct_id)

        if objct_key not in obj_dictionary:
            print("** no instance found **")
            return

        if len(argz) < 3:
            print("** attribute name missing **")
            return
        attrib_name = argz[2]

        if len(argz) < 4:
            print("** value missing **")
            return
        attrib_value = argz[3]
        obj = obj_dictionary[objct_key]
        if hasattr(obj, attrib_name):
            setattr(obj, attrib_name, attrib_value)
            obj.save()
        else:
            setattr(obj, attrib_name, attrib_value)
            obj.save()

    def do_all(self, argument):
        """Print all objects str representation """
        cls_name = argument.split()[0] if argument else None
        objct_list = []

        if cls_name and cls_name not in HBNBCommand.validClasses:
            print("** class doesn't exist **")
        else:
            for objct in storage.all().values():
                if not cls_name or cls_name == objct.__class__.__name__:
                    objct_list.append(str(objct))

            print(objct_list)

    def do_destroy(self, argument):
        """Delete object based on class name and id"""
        argz = argument.split()
        obj_dictionary = storage.all()

        if len(argz) == 0:
            print("** class name missing **")
        elif argz[0] not in HBNBCommand.validClasses:
            print("** class doesn't exist **")
        elif len(argz) == 1:
            print("** instance id missing **")
        else:
            objct = "{}.{}".format(argz[0], argz[1])
            if objct not in obj_dictionary:
                print("** no instance found **")
            else:
                del obj_dictionary[objct]
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
