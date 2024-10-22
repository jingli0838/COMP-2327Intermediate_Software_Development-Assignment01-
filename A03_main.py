"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client

from bank_account import *
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.



client_01 = Client(123, "Lily", "Green", "lilygreen@gmail.com")




# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
chequing_account_01 = ChequingAccount(456, 123, -600.0, date(2024, 8, 1), -100.0, 0.05)

savings_account_01 = SavingsAccount(345, 123, 1559.49, date(2024, 1, 1), 50.0)



# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
chequing_account_01.attach(client_01)
savings_account_01.attach(client_01)




# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
client_02 = Client(666, "Monica", "Geller", "monicageller@gmail.com")
savings_account_02 = SavingsAccount(2389, 666, 782.5, date(2024, 10, 1), 50.0)

savings_account_02.attach(client_02)



# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.


# chequing_account_01
# trigger a large transaction message.
try:
    chequing_account_01.deposit(10000.00)
except ValueError as e:
    print(e)

# no notification
try:
    chequing_account_01.withdraw(1000.0)
except ValueError as e:
    print(e)

# trigger a low balance warning notification
try:
    chequing_account_01.withdraw(8380.0)
except ValueError as e:
    print(e)

# savings_account_01
# trigger a large transaction message.
try:
    savings_account_01.deposit(12000.0)
except ValueError as e:
    print(e)

# no notification
try:
    savings_account_01.withdraw(3000.0)
except ValueError as e:
    print(e)

# trigger a low balance warning notification
try:
    savings_account_01.withdraw(10550.0)
except ValueError as e:
    print(e)


# savings_account_02
# trigger a large transaction message.
try:
    savings_account_02.deposit(11000.0)
except ValueError as e:
    print(e)

# no notification
try:
    savings_account_02.withdraw(2000.0)
except ValueError as e:
    print(e)

# trigger a low balance warning notification
try:
    savings_account_02.withdraw(9750.0)
except ValueError as e:
    print(e)
