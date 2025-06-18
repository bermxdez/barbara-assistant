import json
from datetime import datetime

HISTORY_FILE = "data/history.json"

def save_to_history(city, user):
    entry = {
        "user": user,
        "city": city,
        "timestamp": datetime.now().isoformat()
    }

    try: 
        with open(HISTORY_FILE, "r") as file: 
            data = json.load(file)
    
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(entry)

    with open(HISTORY_FILE, "w") as file:
        json.dump(data, file, indent=2)


def view_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            data = json.load(file)
            if not data:
                print("No search history yet.")
                return

            print("\n🕓 Search History:")
            for entry in data[-10:]:  # últimos 10
                print(f"- {entry['timestamp'][:16]} | {entry['user']} | {entry['city']}")
    except FileNotFoundError:
        print("No history file found.")