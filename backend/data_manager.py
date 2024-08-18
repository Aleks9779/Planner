import json

def load_data(filename='data/planner_data.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data, filename='data/planner_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        
def add_entry(date, activity, hours, earnings):
    data = load_data()
    if date not in data:
        data[date] = []
    data[date].append({'activity': activity, 'hours': hours, 'earnings': earnings})
    save_data(data)
    
def load_categories(filename='data/categories.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_categories(categories, filename='data/categories.json'):
    with open(filename, 'w') as file:
        json.dump(categories, file, indent=4)

def add_category(category):
    categories = load_categories()
    if category not in categories:
        categories.append(category)
        save_categories(categories)