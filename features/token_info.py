import requests
import time
from colorama import init, Fore, Style
import os
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - TOKEN INFO{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def make_request_with_retry(url, headers, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
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
def token_info():
    token = styled_input("Enter the Discord token to look up:")
    if not token:
        print(f"{purple}[ERROR]{white} No token provided. Exiting...{reset}")
        return
    status_message("Looking up token info (trying as user token)")
    headers = {
        "Authorization": token,
        "User-Agent": "Ruin-Token-Info/1.0"
    }
    url = "https://discord.com/api/v9/users/@me"
    response = make_request_with_retry(url, headers)
    if not response or response.status_code != 200:
        print(f"{purple}[INFO]{white} User token authentication failed, trying as bot token...{reset}")
        headers["Authorization"] = f"Bot {token}"
        response = make_request_with_retry(url, headers)
    if not response:
        print(f"{purple}[ERROR]{white} Failed to query the Discord API after multiple attempts.{reset}")
        return
    if response.status_code == 200:
        try:
            user_info = response.json()
            user_id = user_info.get("id", "Unknown")
            username = user_info.get("username", "Unknown")
            discriminator = user_info.get("discriminator", "Unknown")
            email = user_info.get("email", "Not available")
            phone = user_info.get("phone", "Not available")
            mfa_enabled = user_info.get("mfa_enabled", False)
            print(f"{purple}[INFO]{white} Token info retrieved successfully:{reset}")
            print(f"  - User ID: {white}{user_id}{reset}")
            print(f"  - Username: {white}{username}#{discriminator}{reset}")
            print(f"  - Email: {white}{email}{reset}")
            print(f"  - Phone: {white}{phone}{reset}")
            print(f"  - MFA Enabled: {white}{mfa_enabled}{reset}")
        except ValueError:
            print(f"{purple}[ERROR]{white} Failed to parse Discord API response: {response.text}{reset}")
    elif response.status_code == 401:
        print(f"{purple}[ERROR]{white} Invalid token provided. Please check the token and try again.{reset}")
    else:
        print(f"{purple}[ERROR]{white} Failed to query the Discord API: Status {response.status_code}, Response: {response.text}{reset}")
    completion_message("Token Info lookup completed its operations")
def main():
    try:
        token_info()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()