all_vaults = {}

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

print("T Vault")
print("To open a vault account enter '1'")
print("To access belongings in vault enter '2'")
print("To close Vault enter '3'")


first = 0

while True:
    try:
        user_input = int(input(": "))

        if user_input != 1 and first == 0:
            print("you must first creat a vault account")
            continue

        elif user_input == 1:
            name = input("enter your name: ").lower()
            password = input("creat password: ")
            user_vault = SecretVault(name, password) 
            user = user_vault.get_vault(password)
            all_vaults[user] = user_vault
            print(f"{name} vault created")
            first += 1
            
        elif user_input == 2:
            target_vault = input("enter name of vault account: ")

            if target_vault in all_vaults:

                stored_vault = all_vaults[target_vault]
                vault_passcode = input("enter password: ")

                responence = stored_vault.verify(vault_passcode)

                if responence is True:
                    print(f"{target_vault} valut open")
                else:
                    print("password incorrect or valut does not exist")
            else:
                print("check user name, account does not exist")
        elif user_input == 3:
            print("Vault closed")
            break

        else:
            print("read the instruction given above for valid starter input")
            continue

    except ValueError:
        print("invalid input")
        continue