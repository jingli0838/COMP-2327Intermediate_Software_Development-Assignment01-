from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from bank_account import bank_account
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    This class represents a window for searching and managing client accounts.
    """
    def __init__(self):
        """
        Initialize the ClientLookupWindow.
        """
        super().__init__()
        self.__client_listing = {}
        self.__accounts ={}
        data = load_data()
        self.__client_listing = data[1]
        self.__accounts = data[0]
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)
        # Disable filtering widgets initially
        self.filter_combo_box.setEnabled(False)
        self.filter_edit.setEnabled(False)
        self.filter_button.setEnabled(False)

        

    
    def __on_lookup_client(self):
        """
        A function to search for a client by their client number and display their information.
        """
        try:
            # Attempt to convert input to an integer
            client_number = int(self.client_number_edit.text())
        except ValueError:
            # Clear the window using reset_display()
            self.reset_display()
            # Show an error message if input is not numeric
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("The client number must be a numeric value")
            msg.setWindowTitle("Input Error")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        
        if  client_number not in self.__client_listing:
            self.reset_display()
            # Show an error message if input is not numeric
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f'Client number:{client_number} not found.')
            msg.setWindowTitle("Not Found")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        else:
            #set the client_info_label to the Client Name 
            client_object = self.__client_listing[client_number]
            self.client_info_label.setText(f"Client Name: {client_object.first_name} {client_object.last_name}")
        
        # Clear the account table
        self.account_table.setRowCount(0)

        for account_number, account  in self.__accounts.items():
            if account.client_number == client_number:

                account_number_item = QTableWidgetItem(str(account_number))
                balance_item = QTableWidgetItem(f'${account.balance:,.2f}')
                date_created_item = QTableWidgetItem(account._date_created.strftime("%Y-%m-%d"))
                account_type_item = QTableWidgetItem(account.__class__.__name__)
                # Align text to the center for better appearance
                account_number_item.setTextAlignment(Qt.AlignHCenter) 
                balance_item.setTextAlignment(Qt.AlignHCenter) 
                date_created_item.setTextAlignment(Qt.AlignHCenter) 
                account_type_item.setTextAlignment(Qt.AlignHCenter) 
                # Insert the row into the account table
                row_count = self.account_table.rowCount()
                self.account_table.insertRow(row_count)
                # Add items to the table
                self.account_table.setItem(row_count, 0, account_number_item)
                self.account_table.setItem(row_count, 1, balance_item)
                self.account_table.setItem(row_count, 2, date_created_item)
                self.account_table.setItem(row_count, 3, account_type_item)
        self.account_table.resizeColumnsToContents()

        self.__toggle_filter(False)

    @Slot(int, int)          
    def __on_select_account(self, row: int, column: int) ->None:
        """
        a function that handles the selection of an account in the account table.

        Args:
            row (int): The row index of the selected cell in the account table.
            column (int): The column index of the selected cell in the account table.
        """
        #selected_table_row = self.account_table.currentRow()
        account_number = self.account_table.item(row,0).text()
        if len(account_number.strip())== 0:
            # Clear the window using reset_display()
            self.reset_display()
            # Show an error message if input is not numeZric
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Please select a valid record.")
            msg.setWindowTitle("Invalid Selection")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        
        if int(account_number) not in self.__accounts:
            # Clear the window using reset_display()
            self.reset_display()
            # Show an error message if input is not numeric
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Bank Account selected does not exist.")
            msg.setWindowTitle("No Bank Account")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()
            return
        bank_account = self.__accounts[int(account_number)]
        account_details_window = AccountDetailsWindow(bank_account)
        #connect the Signal object of the AccountDetailsWindow instance to the update_data method
        account_details_window.balance_updated.connect(self.__update_data)
        account_details_window.exec()

            
    def __update_data(self,account: BankAccount):
        """
        Updates the account_table, accounts dictionary, and accounts.csv file
        with the latest data for the given BankAccount.
        
        Args:
            account (BankAccount): The updated bank account object.
        """
        # Loop through the account_table widget
        for row in range(self.account_table.rowCount()):
            # Get the account number from the object
            account_number = account.account_number
            if account_number == int(self.account_table.item(row,0).text()):
                # Update the second column (Balance) with the updated balance
                self.account_table.item(row, 1).setText(f"${account.balance:,.2f}")
                # Break the loop since we found the matching account
                break
        
        # Update the corresponding entry in the accounts dictionary
        self.__accounts[account.account_number] = account

        # Invoke the update_data function of the manage_data module
        update_data(account)

    def __on_filter_clicked(self):
        """
        Handles the click event of the filter button.
        """

        if self.filter_button.text() == "Apply Filter":
            column_table_index = self.filter_combo_box.currentIndex()

            filter_value = self.filter_edit.text()
            # Loop through the account_table widget
            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row,column_table_index)
                if item and filter_value in item.text():
                    # Show the row if it matches the filter
                    self.account_table.setRowHidden(row, False) 
                else:
                    # Hide the row if it doesn't match the filter
                    self.account_table.setRowHidden(row,True)
            self.__toggle_filter(True)
        else:
            # Show all rows
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False) 

            self.__toggle_filter(False)

    def __toggle_filter(self, filter_on):
        """
        Toggles the filter state and updates the UI accordingly.

        Args:
            filter_on(bool): to indicate whether the filter is currently active.
        """
        if filter_on == True:
            self.filter_button.setText("Reset") 
            self.filter_button.setEnabled(True)
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered") 
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_button.setEnabled(True)
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_label.setText("Data is Not Currently Filtered") 

        


        

                

                    



        






        











            













    


        