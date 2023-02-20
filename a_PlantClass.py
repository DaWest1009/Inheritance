
class Plant:  # superclass
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color


class Flower(Plant):  # subclass for Plant superclass
    def __init__(self, color, petals):
        Plant.__init__(self, color)  # init method of subclass will always
        # call init method of superclass
        self.__petals = petals

    def get_petals(self):
        return self.__petals
