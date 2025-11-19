
class Vault:
    def __init__(self, username):
        self.username = username
        self.greeting(username)
    
    def login(self, username):
        try:
            with open(f'./vault/{username}.vault', 'x'):
                print(f'created new user: {username}')
        except FileNotFoundError:
            print('FileNotFoundError, probably missing ".vault" directory?') 
            print('hint: mkdir vault')
            quit()
        except:
            pass

    def greeting(self, username):
        print("\033[2J\033[H")
        self.login(username)
        print("--- Password manager ---")
        print(f"hello, {username}")

if __name__ == "__main__":
    print("--- Password manager ---")
    username = str(input("username: "))
    Vault(username)

