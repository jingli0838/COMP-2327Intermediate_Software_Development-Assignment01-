"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: {Jing Li}
Date: {10/02/2024}
"""

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(123, 456, -600.0, date(2024, 8, 1), -100.0, 0.05)


# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account)
print(f'service charges: ${chequing_account.get_service_charges():.2f}')


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.

chequing_account.deposit(1000.0)

print(chequing_account)

print(f'service charges: ${chequing_account.get_service_charges():.2f}')


print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.

savings_account = SavingsAccount(9483914, 345, 1559.49, date(2024, 1, 1), 50.0)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

print(savings_account)
print(f'service charges: ${savings_account.get_service_charges():.2f}')

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.

savings_account.withdraw(1520.00)
print(savings_account)
print(f'service charges: ${savings_account.get_service_charges():.2f}')

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account_01 = InvestmentAccount(2341234, 456, 19329.21, date(2024, 1, 1), 1.99)


# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.

print(investment_account_01)
print(f'service charges: ${investment_account_01.get_service_charges():,.2f}')


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.

investment_account_02 = InvestmentAccount(2341234, 456, 18300.21, date(2013, 1, 1), 1.99)


# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_account_02)

print(f'service charges: ${investment_account_02.get_service_charges():.2f}')


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.

chequing_account.withdraw(chequing_account.get_service_charges())

savings_account.withdraw(savings_account.get_service_charges())

investment_account_01.withdraw(investment_account_01.get_service_charges())

investment_account_02.withdraw(investment_account_02.get_service_charges())


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.

print(chequing_account)
print()
print(savings_account)
print()
print(investment_account_01)
print()
print(investment_account_02)