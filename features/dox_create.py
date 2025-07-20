import os
from colorama import init, Fore, Style
from datetime import datetime
import random
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - DOX CREATE{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def dox_create():
    status_message("Gathering target information")
    print(f"\n{purple}[INFO]{white} Basic Information:{reset}")
    target_info = {}
    target_info["Doxed By"] = styled_input("Doxed By (Your Alias):")
    target_info["Reason"] = styled_input("Reason for Dox:")
    target_info["Primary Alias"] = styled_input("Primary Alias/Pseudo:")
    target_info["Secondary Alias"] = styled_input("Secondary Alias/Pseudo:")
    print(f"\n{purple}[INFO]{white} Personal Information:{reset}")
    target_info["First Name"] = styled_input("First Name:")
    target_info["Last Name"] = styled_input("Last Name:")
    target_info["Gender"] = styled_input("Gender:")
    target_info["Age"] = styled_input("Age:")
    target_info["Date of Birth"] = styled_input("Date of Birth (e.g., YYYY-MM-DD):")
    target_info["Occupation"] = styled_input("Occupation:")
    target_info["Education"] = styled_input("Education (e.g., School/University):")
    print(f"\n{purple}[INFO]{white} Contact Information:{reset}")
    target_info["Phone Number"] = styled_input("Phone Number:")
    target_info["Email Address"] = styled_input("Email Address:")
    target_info["Alternative Email"] = styled_input("Alternative Email Address:")
    target_info["Phone Brand"] = styled_input("Phone Brand/Model (if known):")
    print(f"\n{purple}[INFO]{white} Location Information:{reset}")
    target_info["Continent"] = styled_input("Continent:")
    target_info["Country"] = styled_input("Country:")
    target_info["Region/State"] = styled_input("Region/State:")
    target_info["City"] = styled_input("City:")
    target_info["Postal Code"] = styled_input("Postal Code:")
    target_info["Address"] = styled_input("Address:")
    target_info["Timezone"] = styled_input("Timezone:")
    target_info["Latitude"] = styled_input("Latitude (if known):")
    target_info["Longitude"] = styled_input("Longitude (if known):")
    print(f"\n{purple}[INFO]{white} Social Media Information:{reset}")
    target_info["Social Media Profiles"] = styled_input("Social Media Profiles (comma-separated, e.g., Twitter: @user, Instagram: user):")
    target_info["Known Usernames"] = styled_input("Known Usernames (comma-separated):")
    print(f"\n{purple}[INFO]{white} Online Accounts Information:{reset}")
    target_info["Known Emails"] = styled_input("Known Emails (comma-separated):")
    target_info["Known Passwords"] = styled_input("Known Passwords (comma-separated):")
    target_info["Gaming Accounts"] = styled_input("Gaming Accounts (e.g., Roblox, Steam, etc.):")
    target_info["Other Accounts"] = styled_input("Other Online Accounts (e.g., PayPal, Amazon, etc.):")
    print(f"\n{purple}[INFO]{white} Discord Information:{reset}")
    target_info["Discord Username"] = styled_input("Discord Username (e.g., user#1234):")
    target_info["Discord Display Name"] = styled_input("Discord Display Name:")
    target_info["Discord ID"] = styled_input("Discord ID:")
    target_info["Discord Token"] = styled_input("Discord Token (if known):")
    target_info["Discord Email"] = styled_input("Discord Email (if known):")
    target_info["Discord Phone"] = styled_input("Discord Phone (if known):")
    target_info["Discord Nitro"] = styled_input("Discord Nitro Status (e.g., None, Nitro Classic, Nitro Boost):")
    target_info["Discord Friends"] = styled_input("Discord Friends (comma-separated):")
    target_info["Discord MFA"] = styled_input("Discord MFA Enabled (True/False):")
    print(f"\n{purple}[INFO]{white} Network Information:{reset}")
    target_info["Public IP"] = styled_input("Public IP Address:")
    target_info["Local IP"] = styled_input("Local IP Address:")
    target_info["IPv6"] = styled_input("IPv6 Address (if applicable):")
    target_info["ISP"] = styled_input("ISP (Internet Service Provider):")
    target_info["VPN Usage"] = styled_input("VPN Usage (Yes/No):")
    print(f"\n{purple}[INFO]{white} Device Information:{reset}")
    target_info["Device Name"] = styled_input("Device Name (e.g., PC Name):")
    target_info["Device Username"] = styled_input("Device Username:")
    target_info["Operating System"] = styled_input("Operating System (e.g., Windows 11):")
    target_info["Windows Key"] = styled_input("Windows Product Key (if applicable):")
    target_info["MAC Address"] = styled_input("MAC Address:")
    target_info["HWID"] = styled_input("HWID (Hardware ID):")
    target_info["CPU"] = styled_input("CPU (e.g., Intel i7-9700K):")
    target_info["GPU"] = styled_input("GPU (e.g., NVIDIA RTX 3080):")
    target_info["RAM"] = styled_input("RAM (e.g., 16GB):")
    target_info["Storage"] = styled_input("Storage (e.g., 1TB SSD):")
    target_info["Main Monitor"] = styled_input("Main Monitor (e.g., Dell 27-inch):")
    target_info["Secondary Monitor"] = styled_input("Secondary Monitor (if applicable):")
    print(f"\n{purple}[INFO]{white} Family Information:{reset}")
    target_info["Mother"] = styled_input("Mother's Name:")
    target_info["Father"] = styled_input("Father's Name:")
    target_info["Siblings"] = styled_input("Siblings (comma-separated):")
    target_info["Known Associates"] = styled_input("Known Associates (comma-separated):")
    print(f"\n{purple}[INFO]{white} Other Information:{reset}")
    target_info["Databases"] = styled_input("Known Databases (e.g., breach data):")
    target_info["Logs"] = styled_input("Known Logs (e.g., chat logs, access logs):")
    target_info["Other Notes"] = styled_input("Other Notes:")
    status_message("Creating dox document")
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dox_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    template = f"""
{'█' * 80}
{'█' * 80}
{'█' * 80}
{'█' * 18}  DOX REPORT - GENERATED BY RUIN  {'█' * 18}
{'█' * 80}
{'█' * 80}
{'█' * 80}

Date Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Doxed By: {target_info['Doxed By'] or 'Not provided'}
Reason: {target_info['Reason'] or 'Not provided'}
Primary Alias: {target_info['Primary Alias'] or 'Not provided'}
Secondary Alias: {target_info['Secondary Alias'] or 'Not provided'}

{'═' * 80}
█  PERSONAL INFORMATION
{'═' * 80}
First Name: {target_info['First Name'] or 'Not provided'}
Last Name: {target_info['Last Name'] or 'Not provided'}
Gender: {target_info['Gender'] or 'Not provided'}
Age: {target_info['Age'] or 'Not provided'}
Date of Birth: {target_info['Date of Birth'] or 'Not provided'}
Occupation: {target_info['Occupation'] or 'Not provided'}
Education: {target_info['Education'] or 'Not provided'}

{'═' * 80}
█  CONTACT INFORMATION
{'═' * 80}
Phone Number: {target_info['Phone Number'] or 'Not provided'}
Phone Brand/Model: {target_info['Phone Brand'] or 'Not provided'}
Email Address: {target_info['Email Address'] or 'Not provided'}
Alternative Email: {target_info['Alternative Email'] or 'Not provided'}

{'═' * 80}
█  LOCATION INFORMATION
{'═' * 80}
Continent: {target_info['Continent'] or 'Not provided'}
Country: {target_info['Country'] or 'Not provided'}
Region/State: {target_info['Region/State'] or 'Not provided'}
City: {target_info['City'] or 'Not provided'}
Postal Code: {target_info['Postal Code'] or 'Not provided'}
Address: {target_info['Address'] or 'Not provided'}
Timezone: {target_info['Timezone'] or 'Not provided'}
Latitude: {target_info['Latitude'] or 'Not provided'}
Longitude: {target_info['Longitude'] or 'Not provided'}

{'═' * 80}
█  SOCIAL MEDIA INFORMATION
{'═' * 80}
Social Media Profiles: {target_info['Social Media Profiles'] or 'Not provided'}
Known Usernames: {target_info['Known Usernames'] or 'Not provided'}

{'═' * 80}
█  ONLINE ACCOUNTS INFORMATION
{'═' * 80}
Known Emails: {target_info['Known Emails'] or 'Not provided'}
Known Passwords: {target_info['Known Passwords'] or 'Not provided'}
Gaming Accounts: {target_info['Gaming Accounts'] or 'Not provided'}
Other Accounts: {target_info['Other Accounts'] or 'Not provided'}

{'═' * 80}
█  DISCORD INFORMATION
{'═' * 80}
Username: {target_info['Discord Username'] or 'Not provided'}
Display Name: {target_info['Discord Display Name'] or 'Not provided'}
User ID: {target_info['Discord ID'] or 'Not provided'}
Token: {target_info['Discord Token'] or 'Not provided'}
Email: {target_info['Discord Email'] or 'Not provided'}
Phone: {target_info['Discord Phone'] or 'Not provided'}
Nitro Status: {target_info['Discord Nitro'] or 'Not provided'}
Friends: {target_info['Discord Friends'] or 'Not provided'}
MFA Enabled: {target_info['Discord MFA'] or 'Not provided'}

{'═' * 80}
█  NETWORK INFORMATION
{'═' * 80}
Public IP: {target_info['Public IP'] or 'Not provided'}
Local IP: {target_info['Local IP'] or 'Not provided'}
IPv6: {target_info['IPv6'] or 'Not provided'}
ISP: {target_info['ISP'] or 'Not provided'}
VPN Usage: {target_info['VPN Usage'] or 'Not provided'}

{'═' * 80}
█  DEVICE INFORMATION
{'═' * 80}
Device Name: {target_info['Device Name'] or 'Not provided'}
Device Username: {target_info['Device Username'] or 'Not provided'}
Operating System: {target_info['Operating System'] or 'Not provided'}
Windows Product Key: {target_info['Windows Key'] or 'Not provided'}
MAC Address: {target_info['MAC Address'] or 'Not provided'}
HWID: {target_info['HWID'] or 'Not provided'}
CPU: {target_info['CPU'] or 'Not provided'}
GPU: {target_info['GPU'] or 'Not provided'}
RAM: {target_info['RAM'] or 'Not provided'}
Storage: {target_info['Storage'] or 'Not provided'}
Main Monitor: {target_info['Main Monitor'] or 'Not provided'}
Secondary Monitor: {target_info['Secondary Monitor'] or 'Not provided'}

{'═' * 80}
█  FAMILY INFORMATION
{'═' * 80}
Mother: {target_info['Mother'] or 'Not provided'}
Father: {target_info['Father'] or 'Not provided'}
Siblings: {target_info['Siblings'] or 'Not provided'}
Known Associates: {target_info['Known Associates'] or 'Not provided'}

{'═' * 80}
█  OTHER INFORMATION
{'═' * 80}
Known Databases: {target_info['Databases'] or 'Not provided'}
Known Logs: {target_info['Logs'] or 'Not provided'}
Other Notes: {target_info['Other Notes'] or 'Not provided'}

{'█' * 80}
█  END OF DOX REPORT
{'█' * 80}
"""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(template)
        print(f"{purple}[INFO]{white} Dox document saved to {filepath}{reset}")
    except Exception as e:
        print(f"{purple}[ERROR]{white} Failed to save dox document: {e}{reset}")
        return
    completion_message("Dox Create completed its operations")
def main():
    try:
        dox_create()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()