import os

class Vault:
    def __init__(self, vault_login):
        self.vault_login = vault_login
        welcome = self.login(vault_login)
        while True:
            self.choice_menu(vault_login, welcome)

    def login(self, vault_login):
        if not os.path.isdir("vault"):
            os.makedirs("vault")
            print("created .vault directory")

        if not os.path.isfile(f"vault/{vault_login}.vault"):
            open(f"vault/{vault_login}.vault", "w")
            print(f"created new user: {vault_login}")
            return "    hello," 
        else: 
            return "    hello again,"

    def choice_menu(self, vault_login, welcome, phraze="", tries=3):
        print("--- Password manager ---")
        print(f"{welcome} {vault_login}")
        print("\n    choose option\n"
              "    1 add entry\n"
              "    2 read entry\n"
              "    3 remove entry\n"
              "    4 help\n"
              "    5 quit\n")
        try:
            choice = int(input(f"--- option: "))

            self.match_choice(choice)
        except ValueError:
            print("\033[2J\033[H")
            phraze = f"option should be a number\n     {tries} tries left\n"
            if tries >= 1:
                print(phraze)
                self.choice_menu(vault_login, "    hello", phraze, tries-1)
                
    def match_choice(self, choice):
        match choice:
            case 1:
                website, username, password = self.entry_info()                
                self.add_entry(vault_login, website, username, password)
            case 2:
                print("\033[2J\033[H")
                self.read_entry(vault_login)
            case 3:
                print("\033[2J\033[H")
                self.remove_entry(vault_login)
            case 4:
                self.help()
            case 5:
                quit()
            case _: 
                print("asd")

    def entry_info(self):
        website = input("    website: ").strip()
        username = input("    username: ").strip()
        password = input("    password: ").strip()
        return website, username, password

    def add_entry(self, vault_login, website, username, password):
        with open(f"vault/{vault_login}.vault", "a") as f:
            f.write(f"{website} {username} {password}\n")

            print("\033[2J\033[H")
            print(f"added entry: {website} {username} {password[: -4]}***** ")
            f.close()

    def read_entry(self, vault_login):
        print("\n--- INDEX | WEBSITE | USERNAME | PASSWORD ---\n")
        with open(f"vault/{vault_login}.vault", "r") as f:
            for index, line in enumerate(f):
                print(f"    {index}: {line}")
            f.close()
        # fix this later        

    def remove_entry(self, vault_login):
        with open(f"vault/{vault_login}.vault", "r") as f:
            self.read_entry(vault_login)
            try:
                remove = int(input("    delete entry: "))
                # fix this later
            except ValueError:
                print("\033[2J\033[H")
                print("    not a number, try again")



    def help(self):
        print("\033[2J\033[H")
        print("    1. add an entry by providing: website username password\n "
              "   2. read all your passwords\n"
              "    3. remove entry by typing it's index number\n"
              "    4. display this menu\n"
              "    5. exit the program\n")

if __name__ == "__main__":
    print("\033[2J\033[H")
    print("--- Password manager ---")
    vault_login = input("    username: ")

    print("\033[2J\033[H")
    Vault(vault_login)

