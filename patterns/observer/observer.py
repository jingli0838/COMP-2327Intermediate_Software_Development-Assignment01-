"""
Description: {This file defines the abstract base class 'Observer' for the observer pattern implementation.
             The Observer class is intended to be inherited by concrete observer classes that wish to receive
             notifications about changes in a 'Subject' (e.g., bank account updates). Each observer implements
             the 'update' method, which is called when the subject changes.}
Author: {Jing Li}
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    """
    An abstract base class representing a observer for receiving any notice of a bank account.
    """
    @abstractmethod
    def update(self, message:str) ->None:
        """
        Abstract method to update the message for significant activities in any of the observer's bank accounts.
        The update method will be implemented in the concrete classes to notify observers when there are changes in the subject.
        Args:
            message (str):  The message for significant activities in any of the observer's bank accounts.
        """
        pass