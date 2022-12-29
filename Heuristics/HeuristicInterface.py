from abc import ABC, abstractmethod


class HeuristicInterface(ABC):
    @abstractmethod
    def calc(self):
        pass
