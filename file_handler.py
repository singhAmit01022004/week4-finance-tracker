import json
import csv
import os
import shutil
from datetime import datetime

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup/"

def save_expenses(expenses):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)

def load_expenses():
    if not os.path.exists(DATA_FILE): return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except: return []

def export_to_csv(expenses, filename="data/exports/expenses_export.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    keys = ["date", "amount", "category", "description"]
    with open(filename, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows([e.to_dict() for e in expenses])

def create_backup():
    if os.path.exists(DATA_FILE):
        os.makedirs(BACKUP_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        shutil.copy(DATA_FILE, f"{BACKUP_DIR}backup_{timestamp}.json")
        return True
    return False