from abc import ABC, abstractmethod
from datetime import datetime


class Account(ABC):

    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.__balance = initial_balance
        self.transactions = []

        if initial_balance > 0:
            self.transactions.append(
                self._create_transaction(
                    "Deposit",
                    initial_balance
                )
            )

    def _create_transaction(self, transaction_type, amount):
        return {
            "type": transaction_type,
            "amount": amount,
            "balance": self.__balance,
            "date": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False

        self.__balance += amount

        self.transactions.append(
            self._create_transaction(
                "Deposit",
                amount
            )
        )

        print(f"₹{amount:.2f} deposited successfully.")
        return True

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if amount > self.__balance:
            print("Insufficient balance.")
            return False

        self.__balance -= amount

        self.transactions.append(
            self._create_transaction(
                "Withdrawal",
                amount
            )
        )

        print(f"₹{amount:.2f} withdrawn successfully.")
        return True

    def get_balance(self):
        return self.__balance

    def show_details(self):
        print("\n========== ACCOUNT DETAILS ==========")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Account Type:", self.account_type())
        print(f"Balance: ₹{self.__balance:.2f}")

    def show_transactions(self):

        print("\n========== TRANSACTION HISTORY ==========")

        if not self.transactions:
            print("No transactions available.")
            return

        for transaction in self.transactions:
            print(
                f"{transaction['date']} | "
                f"{transaction['type']} | "
                f"₹{transaction['amount']:.2f} | "
                f"Balance: ₹{transaction['balance']:.2f}"
            )

    @abstractmethod
    def account_type(self):
        pass


class SavingsAccount(Account):

    def account_type(self):
        return "Savings Account"

    def calculate_interest(self):
        interest = self.get_balance() * 0.05
        return interest


class CurrentAccount(Account):

    def account_type(self):
        return "Current Account"

    def calculate_interest(self):
        return 0


class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self):

        account_number = input(
            "Enter account number: "
        ).strip()

        if account_number in self.accounts:
            print("Account already exists.")
            return

        name = input(
            "Enter account holder name: "
        ).strip()

        try:
            balance = float(
                input("Enter initial deposit: ")
            )

            if balance < 0:
                print("Initial balance cannot be negative.")
                return

        except ValueError:
            print("Please enter a valid amount.")
            return

        print("\n1. Savings Account")
        print("2. Current Account")

        account_type = input(
            "Choose account type: "
        ).strip()

        if account_type == "1":
            account = SavingsAccount(
                account_number,
                name,
                balance
            )

        elif account_type == "2":
            account = CurrentAccount(
                account_number,
                name,
                balance
            )

        else:
            print("Invalid account type.")
            return

        self.accounts[account_number] = account

        print("\nAccount created successfully!")


    def find_account(self):

        account_number = input(
            "Enter account number: "
        ).strip()

        account = self.accounts.get(account_number)

        if account is None:
            print("Account not found.")
            return None

        return account


    def deposit(self):

        account = self.find_account()

        if account is None:
            return

        try:
            amount = float(
                input("Enter deposit amount: ")
            )

            account.deposit(amount)

        except ValueError:
            print("Please enter a valid amount.")


    def withdraw(self):

        account = self.find_account()

        if account is None:
            return

        try:
            amount = float(
                input("Enter withdrawal amount: ")
            )

            account.withdraw(amount)

        except ValueError:
            print("Please enter a valid amount.")


    def check_balance(self):

        account = self.find_account()

        if account is None:
            return

        print(
            f"Current Balance: "
            f"₹{account.get_balance():.2f}"
        )


    def show_account(self):

        account = self.find_account()

        if account is None:
            return

        account.show_details()


    def show_transactions(self):

        account = self.find_account()

        if account is None:
            return

        account.show_transactions()


    def run(self):

        while True:

            print("\n================================")
            print("       PYTHON BANKING SYSTEM")
            print("================================")

            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Account Details")
            print("6. Transaction History")
            print("7. Exit")

            choice = input(
                "Enter your choice: "
            ).strip()

            if choice == "1":
                self.create_account()

            elif choice == "2":
                self.deposit()

            elif choice == "3":
                self.withdraw()

            elif choice == "4":
                self.check_balance()

            elif choice == "5":
                self.show_account()

            elif choice == "6":
                self.show_transactions()

            elif choice == "7":
                print(
                    "Thank you for using "
                    "Python Banking System!"
                )
                break

            else:
                print("Invalid choice.")


if __name__ == "__main__":

    bank = Bank()
    bank.run()