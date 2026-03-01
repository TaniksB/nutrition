from functions import *
import sys

big_dict = load_from_list()

cmds = (".list", ".wipelist", ".report", ".wipe", ".new", ".q")

usage_message()

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


