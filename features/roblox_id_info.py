import requests
from colorama import init, Fore, Style
import os
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - ROBLOX ID INFO{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def make_request_with_retry(method, url, headers=None, max_retries=5):
    if headers is None:
        headers = {"User-Agent": "Ruin-Roblox-ID-Info/1.0"}
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
def roblox_id_info():
    user_id = styled_input("Enter the Roblox user ID to look up:")
    if not user_id:
        print(f"{purple}[ERROR]{white} No user ID provided. Exiting...{reset}")
        return
    try:
        user_id = int(user_id)
        if user_id <= 0:
            raise ValueError
    except ValueError:
        print(f"{purple}[ERROR]{white} Invalid user ID. Must be a positive integer.{reset}")
        return
    status_message(f"Fetching info for user ID: {user_id}")
    url = f"https://users.roblox.com/v1/users/{user_id}"
    response = make_request_with_retry("GET", url)
    if not response or response.status_code != 200:
        print(f"{purple}[ERROR]{white} Failed to fetch user info: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
        return
    try:
        user_info = response.json()
        username = user_info.get("name", "Unknown")
        display_name = user_info.get("displayName", "Unknown")
        description = user_info.get("description", "Not set")
        created = user_info.get("created", "Unknown")
        is_banned = user_info.get("isBanned", False)
    except ValueError:
        print(f"{purple}[ERROR]{white} Failed to parse user info response: {response.text}{reset}")
        return
    print(f"{purple}[INFO]{white} Roblox user info for ID {user_id}:{reset}")
    print(f"  - Username: {white}{username}{reset}")
    print(f"  - Display Name: {white}{display_name}{reset}")
    print(f"  - Description: {white}{description}{reset}")
    print(f"  - Created: {white}{created}{reset}")
    print(f"  - Is Banned: {white}{is_banned}{reset}")
    completion_message("Roblox ID Info lookup completed its operations")
def main():
    try:
        roblox_id_info()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()