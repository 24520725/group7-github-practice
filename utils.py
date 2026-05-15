import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def press_enter_to_continue():
    input("Press Enter to continue...")