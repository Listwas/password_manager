import sys
sys.path.append('./vault')
from cli import menu_loop

if __name__ == "__main__":
    username = input("vault username: ").strip()
    menu_loop(username)
