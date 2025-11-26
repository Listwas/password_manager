# loading / saving / parsing 
import os

DELIM = "|"

def get_vault_path(username: str) -> str:
    return os.path.join("data", f"{username}.vault")

def load_vault(username: str) -> list[dict]:
    path = get_vault_path(username)
    
    if not os.path.exists("data"):
        os.makedirs("data")
        print("created .data directory")

    if not os.path.isfile(path):
        open(path, "w").close()
        print(f"created user vault in {path}")
        return []

    entries = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(DELIM)
            service, username, password = parts 
            entries.append({
                "service": service,
                "username": username,
                "password": password
            })
    return entries 

def save_vault(username: str, entries: list[dict]) -> None:
    path = get_vault_path(username)

    with open(path, "w") as f:
        for e in entries:
            line = DELIM.join([e["service"], e["username"], e["password"]])
            f.write(line + "\n")
