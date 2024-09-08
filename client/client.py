"""
Description: {description of the file.}
Author: {Jing Li}
"""


from email_validator import ValidatedEmail, EmailNotValidError


class Client:
    def __init__(self,client_number:int, first_name:str, last_name:str, email_address:str):
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
            user_email = ValidatedEmail(email_address)
            self.__email_address = user_email.email
        except EmailNotValidError:
            self.__email_address = "email@pixell-river.com" 
      

    # Getter for client_number
    @property
    def client_number(self)->int:
        return self.__client_number
    # Getter for first_name
    @property
    def first_name(self)->str:
        return self.first_name
    # Getter for last_name
    @property
    def last_name(self)->str:
        return self.last_name
     # Getter for email_address
    @property
    def email_address(self)->str:
        return self.email_address
    
    def __str__(self)->str:
        return f"{self.last_name}, {self.first_name}[{self.client_number}]-{self.email_address}"

    


