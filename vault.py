from datetime import datetime

basic_vaults = {}
premium_vault = {}
class SecretVault:
    def __init__(self, user, password):
        self.user_name = user
        self.__password = None
    
    def get_vault(self, password):
        if len(password) < 8:
            raise ValueError ("password must have more than 8 characters") 
        self.__password = password
        self.user_name
        return self.user_name
    
    def verify(self, attempt):
    
        if attempt == self.__password:
            return True
        else:
            return False
class PremiumVault(SecretVault):
    def __init__(self, user, password, color):
        super().__init__(user, password)
        self.color = color
        self.balance = 0
        self.history = []
    
    def add_deposit(self, amount):
        if amount <= 0:
            raise ValueError("invalid input, you cannot input a negative number") 
        self.balance += amount
        new_record = Transaction("Deposit", amount)
        self.history.append(new_record)

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance = self.balance - amount
            new_record = Transaction("Withdrawal", amount)
            self.history.append(new_record)
            return True
class Transaction:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        self.time = datetime.now().strftime("%H:%M:%S")

    def display(self):
        print(f"[{self.time}] {self.category}: ${self.amount}")

print("T Vault")
print("To open a vault account enter '1'")
print("To access belongings in vault enter '2'")
print("To withdraw enter '3'")
print("To check transaction history enter '4'")
print("To close Vault enter '5'")


first = 0

while True:
    try:
        user_input = int(input(": "))

        if user_input != 1 and first == 0:
            print("you must first creat a vault account")
            continue

        elif user_input == 1:
            print("enter 1 to open a static account")
            print("enter 2 to open a premium account, which allows deposits")
            type_acc = int(input(":"))

            if type_acc == 1:
                name = input("enter your name: ").lower()
                password = input("creat password: ")
                user_vault = SecretVault(name, password) 
                user = user_vault.get_vault(password)
                basic_vaults[user] = user_vault
                print(f"{name} vault created")
                first += 1

            elif type_acc == 2:
                name = input("enter your name: ").lower()
                password = input("creat password: ")
                vault_color = input("what color of vault would you like: ")
                user_pre_vault = PremiumVault(name, password, vault_color)
                user = user_pre_vault.get_vault(password)
                first += 1

                premium_vault[user] = user_pre_vault

                ans = input("would you like to fund account: ").lower()
                if ans == "yes":
                    how_much = int(input("how much: "))
                    balance = user_pre_vault.add_deposit(how_much)

                print(f"{name} vault account opened")
            else:
                print("invalid input!")
                continue

        elif user_input == 2:
            what = input("which type of vault account do you have(basic/premium): ").lower()
            if what == "basic":
                target_vault = input("enter name of vault account: ")

                if target_vault in basic_vaults:

                    stored_vault = basic_vaults[target_vault]
                    vault_passcode = input("enter password: ")

                    responence = stored_vault.verify(vault_passcode)

                    if responence is True:
                        print(f"{target_vault} valut open")
                    else:
                        print("password incorrect or valut does not exist")
                else:
                    print("check user name, account does not exist")
            elif what == "premium":
                target_vault = input("enter name of vault account: ")

                if target_vault in premium_vault:

                    stored_pvault = premium_vault[target_vault]
                    vault_passcode = input("enter password: ")

                    responence = stored_pvault.verify(vault_passcode)

                    if responence is True:
                        print(f"{target_vault} valut open")
                        print(f"balance: {stored_pvault.balance}")
                        print(f"color: {stored_pvault.color}")
                    else:
                        print("password incorrect or valut does not exist")
                else:
                    print("check user name, account does not exist")
            else:
                print("invalid input")
                continue
        elif user_input == 3:
            _name = input("you can only check the balanse of a premium account, do you have one(yes/no): ").lower()
            if _name == "yes":
                name_user = input("enter your account user name: ").lower()
                if name_user in premium_vault:
                    stored_value = premium_vault[name_user]
                    pass_code = input("enter password: ")
                    verify = stored_value.verify(pass_code)

                    if verify == True:
                        how_much = int(input("how much do you want to withdraw: "))
                        withdrawal = stored_value.withdraw(how_much)

                        if withdrawal == True:
                            print("withdrawal successful")
                        else:
                            print("insufficient funds")
            else:
                print("open a premium account to deposit and withdraw")
                continue
        elif user_input == 4: 
            target = input("Vault Name: ")
            if target in premium_vault:
                vault = premium_vault[target]
        
                print(f"--- Transaction History for {target} ---")
                for record in vault.history:
                    record.display()
        elif user_input == 5:
            print("Vault closed")
            break

        else:
            print("read the instruction given above for valid starter input")
            continue

    except ValueError:
        print("invalid input")
        continue