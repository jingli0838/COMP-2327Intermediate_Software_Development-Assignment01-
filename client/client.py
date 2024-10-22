"""
Description: {This is a `Client` class, representing a client with a client number, first name, 
last name, and email address. 
Author: {Jing Li}
Date: 9/10/2024
"""


from datetime import datetime
from email_validator import validate_email, EmailNotValidError

from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email


class Client(Observer):
    """
    This is a class representing a client

    Attributes: 
        client_number (int): A unique identifier for the client.
        first_name(str): the client's first name.
        last_name(str): the client's last name.
        email_address(str): the clients's email address.

    """
    
    def __init__(self,client_number:int, first_name:str, last_name:str, email_address:str):
        """
        Initializes a Client instance with a client number, first name, last name and email address.
        Args:
            client_number (int): a unique integer identifier for the client.
            first_name (str): the client's first name.
            last_name (str): the cilent's last name.
            email_address (str): the client's email address. if the email address is invalid, 
            the default email address("email@pixell-river.com")  is assigned.

        Raises:
            ValueError: if client number is not an integer.
            ValueError: if first name is blank.
            ValueError: if last name is blank.
        """
        # Initializes the client with client details according to the class diagram
        if isinstance(client_number,int):
            self.__client_number = client_number
        else:
            raise ValueError ("client number should be an integer number ")
       
       #set the attribute representing the first name to the stripped value of the corresponding argument
        striped_first_name = first_name.strip()
        if len(striped_first_name)>0:
            self.__first_name = striped_first_name
        else:
            raise ValueError("first name should not be blank")
       
       #set the attribute representing the last name to the stripped value of the corresponding argument.
        striped_last_name = last_name.strip()
        if len(striped_last_name)>0:
            self.__last_name = striped_last_name
        else:
            raise ValueError("last name should not be blank")
       
        try:
            user_email = validate_email(email_address)
            self.__email_address = user_email.email
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com" 
      

    # Getter for client_number
    @property
    def client_number(self)->int:
        """
        get the client number

        Returns:
            int: client number
        """
        return self.__client_number
    # Getter for first_name
    @property
    def first_name(self)->str:
        """_
        get the first name of the client

        Returns:
            str: the client's first name

        """
        return self.__first_name
    # Getter for last_name
    @property
    def last_name(self)->str:
        """
        get the last name of the client

        Returns:
            str: the client's last name
        """
        return self.__last_name
     # Getter for email_address
    @property
    def email_address(self)->str:
        """
        get the email address of the client

        Returns:
            str: the client's email address
        """
        return self.__email_address
    
    def __str__(self)->str:
        """
        A formated string representation of the client object.

        Returns:
            str: A formated string displaying the client's last name, first name, client number and email address. 
        """
        return f"{self.last_name}, {self.first_name}[{self.client_number}]-{self.email_address}"
    
    def update(self, message:str) -> None:
        """
        Performs some action when the observer is notified.
        Sends a simulated email with a notification message.
        
        Args:
            message (str): The notification message describing the update.
        """
        current_time = datetime.now()
        subject = f'ALERT: Unusual Activity: {current_time}'

        body = f'Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}'
        simulate_send_email(self.email_address, subject, body)



    


