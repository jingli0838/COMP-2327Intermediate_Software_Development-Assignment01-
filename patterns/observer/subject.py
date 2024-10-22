"""
Description:This file defines the 'Subject' class, which serves as the base class in the observer pattern implementation.
            The Subject class maintains a list of observers and provides methods to attach, detach, and notify them
            of any significant changes or events. It is designed to be inherited by specific subjects, such as a bank account,
            that need to notify observers (e.g., clients) about updates or changes.
Author: Jing Li
"""

from abc import ABC
from datetime import date

from patterns.observer.observer import Observer


class Subject(ABC):
    """
    An abstract base class representing a subject in the observer pattern.

    Attributes: 
    _observers[]: a list of observers and provides methods to manage and notify them when certain events occur.
    """
    def __init__(self):
        """
        Initializes a Subject instance with an empty list of observers.
        """
        self._observers = []

    # The attach method is used to add a new observer to the subject's list of observers.
    def attach(self, observer:Observer) -> None:
        """
        A method that attaches an observer to the subject.
        This method adds a new observer to the subject's list of observers, allowing it to receive notifications.

        Args:
            observer (Observer): An observer that wants to be notified of updates.
        """
        self._observers.append(observer)

    # The detach method removes an observer from the subject's list of observers.
    def detach(self, observer:Observer) -> None:
        """
        A method that detaches an observer from the subject.
        This method removes an observer from the subject's list of observers, stopping further notifications to it.

        Args:
            observer (Observer): An observer that no longer wants to receive notifications.
        """
        self._observers.remove(observer)

    def notify(self, message:str) -> None:
        """
        A method that notifies all attached observers with a message.
        This method iterates through the list of observers and calls their 'update' method,
        providing them with the specified message.

        Args:
            message (str): The message containing information about the update or change that should be sent to all observers.
        """
        for observer in self._observers:
            observer.update(message)



        
    