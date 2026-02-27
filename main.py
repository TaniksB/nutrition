from functions import *
import sys

big_dict = load_from_list()

cmds = (".list", ".wipelist", ".report", ".wipe", ".new", ".q")

print ("Usage:")
print (".list - displays list of saved food items")
print (".wipelist - deletes list of saved food items")
print (".report - displays weekly calorie and nutrient report")
print (".wipe - deletes all logged consumption")
print (".new - begins process to save a new food item to list")
print (".q - ends the program")
print ("Any other input will attempt to log consumption")

while 1 < 2:
    inp = input()
    if inp == ".report":
        display_report()
    if inp == ".list":
        display_list()
    if inp == ".wipelist":
        wipe_list()
    if inp == ".wipe":
        wipe_log()
    if inp == ".new":
        list_add()
    if inp == ".q":
        sys.exit()
    if inp not in cmds:
        log_cons(inp)
    inp = None


