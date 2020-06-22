from abc import ABC, abstractmethod


class Cmd(ABC):

    @abstractmethod
    def process(self,*args):
        pass
