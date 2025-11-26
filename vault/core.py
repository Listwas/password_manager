# add / get / list / delete
def add_entry(entries: list[dict], service: str, username: str, password: str):
    entries.append({
        "service": service,
        "username": username,
        "password": password
    })

def get_entry(entries: list[dict], service: str) -> dict | None:
    for e in entries:
        if e["service"] == service:
            return e
    return None

def list_entries(entries: list[dict]) -> list[dict]:
    return entries

def delete_entry(entries: list[dict], index: int) -> bool:
    if 0 <= index < len(entries):
        entries.pop(index)
        return True
    return False
    
