from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, member_id, name):
        self._member_id = member_id
        self._name = name

    @abstractmethod
    def display(self):
        pass