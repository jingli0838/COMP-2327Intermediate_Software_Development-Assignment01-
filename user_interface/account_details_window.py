from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.

    Attributes:
        account: The bank account to be displayed.
    """
    balance_updated = Signal(BankAccount)
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        if isinstance(account, BankAccount):
            # Create a copy of the account
            self.account = copy.copy(account)
            # Set the text for account number and balance labels
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f'${self.account.balance:,.2f}')

            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)
        else:
            self.reject()

    def on_apply_transaction(self):
        """
        This function handles deposit or withdraw transactions on the account.
        It updates the account balance, the display, and emits a balance_updated signal.
        """
        try:
            # Attempt to convert input to a float
            transction_amount = float(self.transaction_amount_edit.text())
        except ValueError:
            # Show an error message if input is not numeric
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Amount must be numeric.")
            msg.setWindowTitle("Invalid Data")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            self.transaction_amount_edit.setFocus()
            return

        try:
            sending_button = self.sender()
            #the sender was the deposit_button
            if sending_button == self.deposit_button:
                operation = "Deposit"
                self.account.deposit(transction_amount)   
            #the sender was the withdraw_button
            if sending_button == self.withdraw_button:
                operation = "Withdraw"
                self.account.withdraw(transction_amount)
            #Update the balance_label widget with the updated balance value of the account attribute
            self.transaction_amount_edit.setText("")
            self.balance_label.setText(f'${self.account.balance:,.2f}')
            self.transaction_amount_edit.setFocus()
        except Exception as e:
            # Show an error message if input is not numeric
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f'{e}')
            msg.setWindowTitle(f'{operation} Failed')
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            self.transaction_amount_edit.setFocus()
            return
        
        self.balance_updated.emit(self.account)


    def on_exit(self):
        """
        This function closes the account details window and returns to the previous window.
        """
        self.close()







