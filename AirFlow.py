# Author: Ryōka
# Contact: @ryukakoi on discord

import os
import time
from colorama import init, Fore, Style
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if not os.path.exists("features"):
    os.makedirs("features")

def display_menu(page):
    purple = Fore.MAGENTA
    white = Fore.WHITE
    reset = Style.RESET_ALL
    ascii_art = f"""
{purple}╔══════════════════════════════════════════════════════════════════╗
{white} /$$$$$$  /$$           /$$$$$$$$ /$$                        
 /$$__  $$|__/          | $$_____/| $$                        
| $$  \ $$ /$$  /$$$$$$ | $$      | $$  /$$$$$$  /$$  /$$  /$$
| $$$$$$$$| $$ /$$__  $$| $$$$$   | $$ /$$__  $$| $$ | $$ | $$
| $$__  $$| $$| $$  \__/| $$__/   | $$| $$  \ $$| $$ | $$ | $$
| $$  | $$| $$| $$      | $$      | $$| $$  | $$| $$ | $$ | $$
| $$  | $$| $$| $$      | $$      | $$|  $$$$$$/|  $$$$$/$$$$/
|__/  |__/|__/|__/      |__/      |__/ \______/  \_____/\___/ 
                                                             
{purple}╚══════════════════════════════════════════════════════════════════╝{reset}
"""
    menu1 = f"""
{ascii_art}
{purple}[ {white}AirFlow - Developed by AirFlow{purple} ]──[ {white}NEXT {white}N {purple}]─{reset}
{purple}┌──────────────────┬────────────────────────┬──────────────────────────┐{reset}
{white}    CORE NUKING            INFO TOOLS               ROBLOX TOOLS         {reset}
{purple}├──────────────────┼────────────────────────┼──────────────────────────┤{reset}
{white} {purple}[{white}01{purple}]{white} Account Nuker    {purple}[{white}04{purple}]{white} Email Lookup       {purple}[{white}07{purple}]{white} Roblox Cookie Info {reset}
{white} {purple}[{white}02{purple}]{white} Server Nuker     {purple}[{white}05{purple}]{white} Token Info         {purple}[{white}08{purple}]{white} Roblox ID Info     {reset}
{white} {purple}[{white}03{purple}]{white} Webhook Nuker    {purple}[{white}06{purple}]{white} Server Info        {purple}[{white}09{purple}]{white} Roblox User Info   {reset}
{purple}└──────────────────┴────────────────────────┴──────────────────────────┘{reset}
{white}> Select Protocol [01-09] or Navigate [N]:{reset}
"""

    menu2 = f"""
{ascii_art}
{purple}[ {white}AirFlow - Developed by AirFlow{purple} ]──[ {white}BACK {white}B {purple}]─{reset}
{purple}┌──────────────────┬───────────────────────┬──────────────────────┐{reset}
{white}       OSINT              GENERATORS               UTILITIES            {reset}
{purple}├──────────────────┼───────────────────────┼──────────────────────┤{reset}
{white} {purple}[{white}10{purple}]{white} Dox Create      {purple}[{white}13{purple}]{white} Token Generator    {purple}[{white}16{purple}]{white} Tool Info          {reset}
{white} {purple}[{white}11{purple}]{white} IP Lookup       {purple}[{white}14{purple}]{white} Nitro Generator    {purple}[{white}17{purple}]{white} User Lookup        {reset}
{white} {purple}[{white}12{purple}]{white} Phone Lookup    {purple}[{white}15{purple}]{white} Roblox Card Gen    {purple}[{white}18{purple}]{white} Terminate          {reset}
{purple}└──────────────────┴───────────────────────┴──────────────────────┘{reset}
{white}> Select Protocol [10-18] or Navigate [B]:{reset}
"""

    if page == 1:
        print(menu1)
    elif page == 2:
        print(menu2)

def main():
    purple = Fore.MAGENTA
    white = Fore.WHITE
    reset = Style.RESET_ALL
    current_page = 1

    while True:
        clear_screen()
        display_menu(current_page)
        choice = input(f"{purple}>>{white} ").strip().lower()

        if choice in ["n", "next"]:
            if current_page == 1:
                current_page = 2
            continue
        elif choice in ["b", "back"]:
            if current_page == 2:
                current_page = 1
            continue

        if choice == "1" or choice == "01":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/account_nuker.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "2" or choice == "02":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/server_nuker.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "3" or choice == "03":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/webhook_nuker.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "4" or choice == "04":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/email_lookup.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "5" or choice == "05":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/token_info.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "6" or choice == "06":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/server_info.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "7" or choice == "07":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/roblox_cookie_info.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "8" or choice == "08":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/roblox_id_info.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "9" or choice == "09":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/roblox_user_info.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")

        elif choice == "10":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/dox_create.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "11":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/ip_lookup.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "12":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/phone_number_lookup.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "13":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/token_generator.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "14":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/nitro_generator.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "15":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/roblox_gift_card_generator.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "16":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/tool_info.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "17":
            print(f"{purple}[EXECUTING]{white} Executing...")
            os.system("python features/username_lookup.py")
            input(f"{purple}[COMPLETE]{white} Press Enter to return...")
        elif choice == "18":
            print(f"{purple}[SHUTDOWN]{white} Terminating AirFlow...")
            time.sleep(1)
            break

        else:
            print(f"{purple}[ERROR]{white} Invalid Command! Check page range.")
            time.sleep(1)
            input(f"{purple}[RETRY]{white} Press Enter to continue...")

if __name__ == "__main__":
    purple = Fore.MAGENTA
    white = Fore.WHITE
    reset = Style.RESET_ALL
    print(f"{purple}[BOOTING]{white} AirFlow - Discord Neural-Net Disruptor Online")
    time.sleep(1)
    main()

