attributes = {
        "name" : None,
        "unit" : None,
        "calories" : 2418,
        "carbs in g" : 274,
        "fat in g" : 62,
        "fibre in g" : 30,
        "protein in g" : 206,
        "A in mcg" : 900,
        #"B1 in mg" : 1.2,
        #"B2 in mg" : 1.3,
        #"B3 in mg" : 16,
        #"B5 in mg" : 5,
        #"B6 in mg" : 1.7,
        #"B7 in mcg" : 30,
        "B9 in mcg" : 400,
        "B12 in mcg" : 2.4,
        "C in mg" : 90,
        "D in mcg" : 20,
        #"E in mg" : 15,
        #"K in mcg" : 120,
        #"Calcium in mg" : 1300,
        #"Chromium in mcg" : 35,
        #"Copper in mg" : 0.9,
        #"Iodine in mcg" : 150,
        "Iron in mg" : 18,
        "Magnesium in mg": 420,
        #"Manganese in mg" : 2.3,
        #"Molybdenum in mcg" : 45,
        #"Phosphorus in mg" : 1250,
        #"Potassium in mg" : 4700,
        #"Selenium in mcg" : 55,
        #"Sodium in mg" : 2300,
        #"Zinc in mg" : 11,
        #"Choline in mg" : 550
}

def usage_message():
    print ("Usage:")
    print (".list - displays list of saved food items")
    print (".wipelist - deletes list of saved food items")
    print (".report - displays weekly calorie and nutrient report")
    print (".wipe - deletes all logged consumption")
    print (".new - begins process to save a new food item to list")
    print (".q - ends the program")
    print ("Any other input will attempt to log consumption")

def sm():
    print ("Enter a command or saved food item:")

import json
import time

def load_from_list():
    with open('/home/yolo/workspace/private/nutrition/list.json', 'r') as fp:
        list_dict = json.load(fp)
        return list_dict

def load_from_clist():
    with open('/home/yolo/workspace/private/nutrition/cons_list.json', 'r') as fp:
        clist = json.load(fp)
        return clist
    
def list_add():
    #print ("began list_add")
    big_dict = load_from_list()
    new_entry = {}
    for a in attributes:
        print (f"Enter {a}:")
        inp = input()
        new_entry[a] = (inp)
    big_dict.append (new_entry)
    save_to_list(big_dict)
    #print ("finished list_add")
    usage_message()
    
def display_report():
    cal = carbs = fat = fibre = protein = va = vb9 = vb12 = vc = vd = iron = magnesium = 0
    dict = load_from_list()
    conslog = load_from_clist()
    legal = load_legal()
    for a in dict:
        cal += int(a["calories"])
        carbs += int(a["carbs in g"])
        fat += int(a["fat in g"])
        fibre += int(a["fibre in g"])
        protein += int(a["protein in g"])
        va += int(a["A in mcg"])
        vb9 += int(a["B9 in mcg"])
        vb12 += int(a["B12 in mcg"])
        vc += int(a["C in mg"])
        vd += int(a["D in mcg"])
        iron += int(a["Iron in mg"])
        magnesium += int(a["Magnesium in mg"])
    print("Consumed the following:")
    for b in conslog:
         name = b
         qty = conslog[b]
         unit = legal[name]
         print(f" - {qty} {unit} of {name}")



def wipe_list():
    print ("This will clear all saved food items. Are you sure? [Y/n]")
    inp = input()
    if inp == "Y":
        dlist = [{}]
        save_to_list(dlist)

def display_list():
    print ("Logged foods:")
    list_dict = load_from_list()
    for a in list_dict:
        print (a["name"])
    #time.sleep(5)
    #usage_message()

def wipe_log():
    clist = {}
    save_to_clist(clist)
    print ("Cleared all logged consumption!")
    
def log_cons(inp):
    legal = load_legal()
    clist = load_from_clist()
    if inp not in legal:
        print (f"{inp} was not found in saved food items!")
    else:
        unit = legal[inp]
        print (clist)
        print (f"Enter {inp} in {unit}:")
        qty = input()
        if qty.isdecimal() == True:
            iqty = int(qty)
        else:
            print ("input must be a whole number!")
            return
        if inp in clist:
            clist[inp] += iqty
        else:
            clist[inp] = iqty
        print (f"Logged {iqty} {unit} of {inp}!")
    save_to_clist(clist)

def save_to_list(dict):
    #print ("began save_to_list")
    with open('/home/yolo/workspace/private/nutrition/list.json', 'w') as fp:
        json.dump(dict, fp)
    #print ("finished save_to_list")

def save_to_clist(clist):
    with open('/home/yolo/workspace/private/nutrition/cons_list.json', 'w') as fp:
        json.dump(clist, fp)

def load_legal():
    list_dict = load_from_list()
    legal = {}
    for a in list_dict:
        b = a["name"]
        c = a["unit"]
        legal[b] = c
    return legal