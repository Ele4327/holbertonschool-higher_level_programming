#!/usr/bin/python3

class Base:

        __nb_objects = 0
        # def init es el constructor: Primera función ejecutada una vez llamada la clase
        def __init__(self, id=None):

                if id != None:
                        self.id = id
                else:
                        Base.__nb_objects += 1
                        self.id = Base.__nb_objects