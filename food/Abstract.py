from abc import ABC,abstractmethod
class Abstractitems(ABC):

    def __init__(self,name,rating = None):
        self.Name = name
        self.Rating = rating