# password manager
a minimal file-based password manager written in python.  
no dependencies, simple cli menus, custom plain-text storage.  
built to practice clean architecture, separation of concerns, and state handling.

## usage
run the app:
python main.py
you will be asked for a vault username.
a vault file will be stored in:
data/<username>.vault

after logging in, the menu looks like this:
1. add entry
2. get entry
3. list entries
4. delete entry
5. quit

entries are stored internally as:
service|username|password

## current features
-add a new credential
-search by service name
-list all stored credentials
-delete an entry by index
-automatic saving on exit

## future roadmap
-encryption 
-hashed master password
-command-line flags
-entry editing

