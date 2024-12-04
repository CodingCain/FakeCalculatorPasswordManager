from pyfiglet import Figlet
import time
import sys
import os


GREEN = "\033[32m"
RED = "\033[31m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Replace with your password or a hint, and what website the password/hint is for
info = {
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint",
            "Website": "password / hint"
            }




format = Figlet(font="Big")


def main():
    while True:
        while True:
            clear_console()
            print(format.renderText("Number Approx Calculator"))
            time.sleep(1)
            print("\n\n")
            while True:
                try:
                    x = float(input("x = ").strip())
                    break
                except ValueError:
                    print("Invalid Format")
                    time.sleep(2)
                    continue
                
            while True:
                try:
                    y = float(input("y = ").strip())
                    break
                except ValueError:
                    print("Invalid Format")
                    time.sleep(2)
                    continue

            print(f"x = {x}   y = {y}")
            operator = input("Choose operator ('+', '-', '*', '/'): ")

            while True:
                if operator in ["+", "-", "*", "/"]:
                    operator = operator[0]
                    break
                
                elif operator == "PASSKEY" and x == 12 and y == 34: # Replace PASSKEY with custom password to enter password manager and replace x and y values with the numbers that will need to be inserted first ie. Pin Number
                    show_info()
            
                else:
                    sys.exit("Invalid Operator")
            
            if operator == "+":
                result = x + y
            elif operator == "-":
                result = x - y
            elif operator == "*":
                result = x * y
            elif operator == "/":
                result = x / y

            rounded_number = round(result / 10) * 10

            print(f"Result = {result}")
            print(f"Rounded to 10 = {rounded_number}") 
            input("Press any key to continue")
            break

                





def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def show_info():
    clear_console()
    menu()
    search = input("> ").lower()
    search_query(search)



    # Menu
# ---- REPLACE WITH NAME OF WEBSITE IN ORDER OF DICT ----
def menu():
    print(format.renderText("| Accounts |"))
    print(
        f"   {YELLOW}1.{RESET} {GREEN}Website{RESET}                       {YELLOW}14.{RESET} {GREEN}Website{RESET}\n"
        f"   {YELLOW}2.{RESET} {GREEN}Website{RESET}                    {YELLOW}15.{RESET} {GREEN}Website{RESET}\n"
        f"   {YELLOW}3.{RESET} {GREEN}Website{RESET}                     {YELLOW}16.{RESET} {GREEN}Website{RESET}\n"
        f"   {YELLOW}4.{RESET} {GREEN}Website{RESET}                  {YELLOW}17.{RESET} {GREEN}Website{RESET}\n"
        f"   {YELLOW}5.{RESET} {GREEN}Website{RESET}                   {YELLOW}18.{RESET} {GREEN}Website{RESET}\n"
        f"   {YELLOW}6.{RESET} {GREEN}Website{RESET}                           {YELLOW}19.{RESET} {GREEN}Website{RESET}\n"
        f"   {YELLOW}7.{RESET} {GREEN}Website{RESET}                        {YELLOW}20.{RESET} {GREEN}Website{RESET}\n"
        f"   {YELLOW}8.{RESET} {GREEN}Website{RESET}                      {YELLOW}21.{RESET} {GREEN}Website{RESET}\n"
        f"   {YELLOW}9.{RESET} {GREEN}Website{RESET}                     {YELLOW}22.{RESET} {GREEN}Website{RESET}\n"
        f"  {YELLOW}10.{RESET} {GREEN}Website{RESET}                       {YELLOW}23.{RESET} {GREEN}Website{RESET}\n"
        f"  {YELLOW}11.{RESET} {GREEN}Website{RESET}                      {YELLOW}24.{RESET} {GREEN}Website{RESET}\n"
        f"  {YELLOW}12.{RESET} {GREEN}Website{RESET}                       {YELLOW}25.{RESET} {GREEN}Website{RESET}\n"
        f"  {YELLOW}13.{RESET} {GREEN}Website{RESET}                       {YELLOW}26.{RESET} {GREEN}Website{RESET}\n\n"
        f"\n                      {RED}27.Exit{RESET}                \n\n"
        )




    # Search

def search_query(search):    

    # Website
    if search == "1" or search == "Website": # Name in Menu
        print("\nAccount: Website") # Name of Account
        print("\nCode: " + info["Website"], end="\n\n") # Name of Key in Dict
        input("Press any key to continue") # Repeat for ALL

    # Website
    elif search == "2" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")
    
    # Website
    elif search == "3" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "4" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "5" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "6" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "7" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "8" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "9" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "10" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "11" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "12" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "13" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "14" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "15" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "16" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "17" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "18" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "19" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "20" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "21" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "22" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "23" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "24" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "25" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Website
    elif search == "26" or search == "Website":
        print("\nAccount: Website")
        print("\nCode: " + info["Website"], end="\n\n")
        input("Press any key to continue")

    # Exit
    elif search == "27" or search == "exit":
        sys.exit("Exiting...")
        time.sleep(1.5)
    else:
        print("Invalid input")
        input("\nPress any key to continue")





if __name__ == "__main__":
    main()