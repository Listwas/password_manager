# menu / input / printing
from core import add_entry, get_entry, list_entries, delete_entry
from storage import load_vault, save_vault

def menu_loop(username: str):
    entries = load_vault(username)

    while True:
        print("\n--- password manager ---")
        print("1. add entry")
        print("2. get entry")
        print("3. list entries")
        print("4. delete entry")
        print("5. quit")

        choice = input("> ")

        if choice == "1":
            service = input("service: ").strip()
            user = input("username: ").strip()
            passwd = input("password: ").strip()
            add_entry(entries, service, user, passwd)

        elif choice == "2":
            service = input("service name: ").strip()
            res = get_entry(entries, service)
            if res:
                print(res)
            else: 
                print("not found")

        elif choice == "3":
            print("\033[2J\033[H")
            print("\n--- stored entries ---")
            for i, e in enumerate(list_entries(entries)):
                print(f"{i} | {e['service']} | {e['username']} | {e['password']}")

        elif choice == "4":
            print("\033[2J\033[H")
            print("\n--- stored entries ---")
            for i, e in enumerate(list_entries(entries)):
                print(f"{i} | {e['service']} | {e['username']} | {e['password']}")
            try: 
                index = int(input("\nindex to delete: "))
                ok = delete_entry(entries, index)
                if not ok:
                    print("invalid index")

            except ValueError:
                print("not a number")
                

        elif choice == "5":
            # print("are you sure you want to save?")
            # print old and new stored entries
            save_vault(username, entries)
            print("data saved\ngoodbye")
            return

        else:
            print("invalid option")



