"""
Description: {description of the file.}
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