"""
Description: {description of the file.}
Author: {Jing Li}
"""

from abc import ABC
from datetime import date

from patterns.observer.observer import Observer


class Subject(ABC):
    def __init__(self):
        
        self._observers = []

    #The attach method is used to add a new observer to the subject's list of observers.
    def attach(self, observer:Observer) -> None:
        self._observers.append(observer)

    #The detach method removes an observer from the subject's list of observers.
    def detach(self, observer:Observer) -> None:
        self._observers.remove(observer)

    def notify(self, message:str) -> None:
        for observer in self._observers:
            observer.update(message)



        
    