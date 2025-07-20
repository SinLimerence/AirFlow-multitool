import requests
from colorama import init, Fore, Style
import os
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - ROBLOX COOKIE INFO{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def make_request_with_retry(method, url, headers, max_retries=5):
    for attempt in range(max_retries):
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, timeout=10)
            else:
                response = None
            if response.status_code == 429:
                retry_after = float(response.headers.get("Retry-After", 1))
                print(f"{purple}[INFO]{white} Rate limited, retrying after {retry_after} seconds...{reset}")
                time.sleep(retry_after)
                continue
            return response
        except requests.exceptions.Timeout:
            print(f"{purple}[ERROR]{white} Request timed out, retrying... (Attempt {attempt + 1}/{max_retries}){reset}")
            if attempt < max_retries - 1:
                time.sleep(2)
            continue
        except requests.exceptions.RequestException as e:
            print(f"{purple}[ERROR]{white} Request failed: {e}, retrying... (Attempt {attempt + 1}/{max_retries}){reset}")
            if attempt < max_retries - 1:
                time.sleep(2)
            continue
    return None
def roblox_cookie_info():
    cookie = styled_input("Enter your Roblox .ROBLOSECURITY cookie:")
    if not cookie:
        print(f"{purple}[ERROR]{white} No cookie provided. Exiting...{reset}")
        return
    headers = {
        "Cookie": f".ROBLOSECURITY={cookie}",
        "User-Agent": "Ruin-Roblox-Cookie-Info/1.0"
    }
    status_message("Fetching user info")
    url = "https://users.roblox.com/v1/users/authenticated"
    response = make_request_with_retry("GET", url, headers)
    if not response or response.status_code != 200:
        print(f"{purple}[ERROR]{white} Failed to authenticate with cookie: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
        return
    try:
        user_info = response.json()
        user_id = user_info.get("id", "Unknown")
        username = user_info.get("name", "Unknown")
        display_name = user_info.get("displayName", "Unknown")
    except ValueError:
        print(f"{purple}[ERROR]{white} Failed to parse user info response: {response.text}{reset}")
        return
    status_message("Fetching Robux balance")
    url = "https://economy.roblox.com/v1/user/currency"
    response = make_request_with_retry("GET", url, headers)
    robux = "Unknown"
    if response and response.status_code == 200:
        try:
            currency_info = response.json()
            robux = currency_info.get("robux", "Unknown")
        except ValueError:
            print(f"{purple}[ERROR]{white} Failed to parse Robux balance response: {response.text}{reset}")
    print(f"{purple}[INFO]{white} Roblox account info:{reset}")
    print(f"  - User ID: {white}{user_id}{reset}")
    print(f"  - Username: {white}{username}{reset}")
    print(f"  - Display Name: {white}{display_name}{reset}")
    print(f"  - Robux Balance: {white}{robux}{reset}")
    completion_message("Roblox Cookie Info lookup completed its operations")
def main():
    try:
        roblox_cookie_info()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()