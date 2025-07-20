import requests
from colorama import init, Fore, Style
import os
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - ROBLOX USER INFO{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def make_request_with_retry(method, url, headers=None, json=None, max_retries=5):
    if headers is None:
        headers = {"User-Agent": "Ruin-Roblox-User-Info/1.0"}
    for attempt in range(max_retries):
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, timeout=10)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=json, timeout=10)
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
def roblox_user_info():
    username = styled_input("Enter the Roblox username to look up:")
    if not username:
        print(f"{purple}[ERROR]{white} No username provided. Exiting...{reset}")
        return
    status_message(f"Converting username {username} to user ID")
    url = "https://users.roblox.com/v1/usernames/users"
    payload = {
        "usernames": [username],
        "excludeBannedUsers": False
    }
    response = make_request_with_retry("POST", url, json=payload)
    if not response or response.status_code != 200:
        print(f"{purple}[ERROR]{white} Failed to convert username to user ID: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
        return
    try:
        data = response.json()
        users = data.get("data", [])
        if not users:
            print(f"{purple}[ERROR]{white} Username {username} not found.{reset}")
            return
        user_id = users[0].get("id", None)
        if not user_id:
            print(f"{purple}[ERROR]{white} Failed to retrieve user ID for username {username}.{reset}")
            return
    except ValueError:
        print(f"{purple}[ERROR]{white} Failed to parse username response: {response.text}{reset}")
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
    print(f"{purple}[INFO]{white} Roblox user info for {username}:{reset}")
    print(f"  - User ID: {white}{user_id}{reset}")
    print(f"  - Username: {white}{username}{reset}")
    print(f"  - Display Name: {white}{display_name}{reset}")
    print(f"  - Description: {white}{description}{reset}")
    print(f"  - Created: {white}{created}{reset}")
    print(f"  - Is Banned: {white}{is_banned}{reset}")
    completion_message("Roblox User Info lookup completed its operations")
def main():
    try:
        roblox_user_info()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()