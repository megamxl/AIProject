from abc import ABC, abstractmethod


class HeuristicInterface(ABC):
    """
    Due to the usage of function Pointers we want a bit of type safety
    and Software Engineering principles
    """
    @abstractmethod
    def calc(self):
        pass
