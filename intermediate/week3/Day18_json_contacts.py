import json
from pathlib import Path

DATA = Path(__file__).with_name("contacts.json")

def load_contacts():
    if DATA.exists():
        return json.loads(DATA.read_text(encoding="utf-8"))
    return []

def save_contacts(contacts):
    DATA.write_text(json.dumps(contacts, indent=2,ensure_ascii=False),encoding="utf-8")

if __name__ == "__main__":
    contacts = load_contacts()
    contacts.append({"name":"Alice","email":"Alice@Wonderland.com"})
    save_contacts(contacts)
    print("Contacts: ", contacts)