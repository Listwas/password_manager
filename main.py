import os

class Vault:
    def __init__(self, vault_login):
        self.vault_login = vault_login

        print("\033[2J\033[H")
        self.login(vault_login)
        self.choice_menu(vault_login)

    def login(self, vault_login):
        if not os.path.isdir("vault"):
            os.makedirs("vault")
            print("created .vault directory")

        if not os.path.isfile(f"vault/{vault_login}.vault"):
            open(f"vault/{vault_login}.vault", "w")
            print(f"created new user: {vault_login}")

    def choice_menu(self, vault_login, phraze="", tries=3):
        print("--- Password manager ---")
        print(f"    hello, {vault_login}") 
        print("\n    choose option\n"
              "    1 add entry\n"
              "    2 read entry\n"
              "    3 remove entry\n"
              "    4 help\n"
              "    5 quit\n")
        try:
            choice = int(input(f"--- option: "))
        except ValueError:
            print("\033[2J\033[H")
            phraze = f"option should be a number\n     {tries} tries left\n"
            if tries >= 1:
                print(phraze)
                self.choice_menu(vault_login, phraze, tries-1)
            quit()
        match choice:
            case 1:
                website, username, password = self.entry_info()                
                self.add_entry(vault_login, website, username, password )
            case 2:
                self.read_entry(vault_login)
            case _:
                return 0
            
    def entry_info(self):
        website = input("    website: ").strip()
        username = input("    username: ").strip()
        password = input("    password: ").strip()
        return website, username, password

    def add_entry(self, vault_login, website, username, password):
        with open(f"vault/{vault_login}.vault", "a") as f:
            f.write(f"{website} {username} {password}\n")
            f.close()

    def read_entry(self, vault_login):
        print("\n--- INDEX | WEBSITE | USERNAME | PASSWORD ---\n")
        with open(f"vault/{vault_login}.vault", "r") as f:
            for index, line in enumerate(f):
                print(f"    {index}: {line}")
        # fix this later        
            
if __name__ == "__main__":
    print("--- Password manager ---")
    vault_login = input("    username: ")
    Vault(vault_login)

# later
# add different msg for returning user
