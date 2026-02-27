attributes = {
        "name" : None,
        "unit" : None,
        "carbs in g" : 274,
        "fat in g" : 62,
        "fibre in g" : 30,
        "protein in g" : 206,
        "A in mcg" : 900,
        "B1 in mg" : 1.2,
        "B2 in mg" : 1.3,
        "B3 in mg" : 16,
        "B5 in mg" : 5,
        "B6 in mg" : 1.7,
        "B7 in mcg" : 30,
        "B9 in mcg" : 400,
        "B12 in mcg" : 2.4,
        "C in mg" : 90,
        "D in mcg" : 20,
        "E in mg" : 15,
        "K in mcg" : 120,
        "Calcium in mg" : 1300,
        "Chromium in mcg" : 35,
        "Copper in mg" : 0.9,
        "Iodine in mcg" : 150,
        "Iron in mg" : 18,
        "Magnesium in mg": 420,
        "Manganese in mg" : 2.3,
        "Molybdenum in mcg" : 45,
        "Phosphorus in mg" : 1250,
        "Potassium in mg" : 4700,
        "Selenium in mcg" : 55,
        "Sodium in mg" : 2300,
        "Zinc in mg" : 11,
        "Choline in mg" : 550
}

import json

def load_from_list():
    with open('list.json', 'r') as fp:
        list_dict = json.load(fp)
        return list_dict
    
def list_add():
    from main import big_dict
    new_entry = {}
    for a in attributes:
        print (f"Enter {a}:")
        inp = input()
        new_entry[a] = (inp)
    big_dict.append (new_entry)
    save_to_list(big_dict)
    
def display_report():
    print ("to be implemented")
    return None

def wipe_list():
    print ("to be implemented")
    return None

def display_list():
    print ("Logged foods:")
    list_dict = load_from_list()
    print (list_dict)

def wipe_log():
    print ("to be implemented")
    return None
    
def log_cons(inp):
    print ("to be implemented")
    return None

def save_to_list(dict):
    with open('list.json', 'w') as fp:
        json.dump(dict, fp)