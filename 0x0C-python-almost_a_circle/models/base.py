#!/usr/bin/python3

class Base:

    """
        Define a "Base" of all clases of the project, base model

        Attributes:
            __nb_objects (int): Number of objects(instances)
    """
    __nb_objects = 0

    def __init__(self, id=None):

        """Constructor to initialice a new instance of base.

        Args:
            id (int): ID of each base instance

        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
