# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each 
assignment will build on the work done in the previous assignment(s).  Ultimately, 
an entire system will be created to manage bank transactions for clients who 
have one or more bank accounts.

## Author
[Jing Li]

## Assignment
Assignment [01] [This assignment will produce some foundational classes to be used in an overall system. The classes will incorporate the outcomes associated with Module 01. Specifically, these classes will incorporate encapsulation through the use of private attributes and public accessors and mutators. Additionally, these classes will benefit from thorough unit testing, including unit test planning. The classes developed in this assignment will contribute to upcoming assignments. ]

Assignment[02] [This assignment will extend the BankAccount class created in your previous assignment. The BankAccount class will be used as a superclass from which more specific subclasses will be derived. Each subclass will inherit attributes and methods from the superclass, and will incorporate functionality specific to the subclass. Polymorphism will be realized by having each subclass provide their own unique implementation to a superclass method. Unit testing in this assignment will be limited to verifying the expected polymorphic behaviour.]

Assignment [3]: This assignment will address issues associated with the scalability and maintainability of the current service charge calculation functionality.

Assignment [4]: This assignment will incorporate a Graphical User Interface (GUI) into the PiXELL-River Financial banking system. The end product will include a lookup window from which users can view existing Client and corresponding Bank Account data. The user can then select a Bank Account and perform deposit and withdraw transactions against the selected Bank Account. 


## Encapsulation
[Encapsulation is one of the fundamental principles of object-oriented programming. It refers to the practice of bundling the data (attributes) and methods (functions) that operate on that data into a single unit, usually a class, and restricting direct access to some of the object's components. This is done to protect the internal state of an object and provide controlled access to it.]

##  Polymorphism
[Polymorphism is a core concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass, even if those objects behave differently. In the context of the BankAccount class and its subclasses (ChequingAccount, SavingsAccount, InvestmentAccount), polymorphism is achieved by overriding methods in the subclasses to provide specific behaviors while still maintaining a common interface.]