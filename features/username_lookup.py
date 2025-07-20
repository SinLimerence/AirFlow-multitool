import os
import time
import requests
from datetime import datetime
from colorama import init, Fore, Style
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - USERNAME LOOKUP{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def check_username(platform, username, url_template):
    try:
        url = url_template.format(username=username)
        response = requests.get(url, timeout=5, headers={"User-Agent": "Ruin-Username-Lookup/1.0"})
        if response.status_code == 200:
            return True, url
        return False, url
    except requests.exceptions.RequestException:
        return False, url_template.format(username=username)
def username_lookup():
    username = styled_input("Enter the username to search for:")
    if not username:
        print(f"{purple}[ERROR]{white} No username provided. Exiting...{reset}")
        return
    platforms = {
        "Twitter": "https://twitter.com/{}",
        "Instagram": "https://www.instagram.com/{}",
        "GitHub": "https://github.com/{}",
        "Reddit": "https://www.reddit.com/user/{}",
        "Twitch": "https://www.twitch.tv/{}",
        "YouTube": "https://www.youtube.com/@{}"
    }
    status_message(f"Searching for username '{username}' across platforms")
    found_results = []
    for platform, url_template in platforms.items():
        found, url = check_username(platform, username, url_template)
        if found:
            print(f"{purple}[FOUND]{white} {platform}: {url}{reset}")
            found_results.append((platform, url))
        else:
            print(f"{purple}[NOT FOUND]{white} {platform}: {url}{reset}")
        time.sleep(0.5)
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"username_lookup_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Username Lookup Results for '{username}'\n")
            f.write("=" * 35 + "\n\n")
            if found_results:
                f.write("Found on the following platforms:\n")
                for platform, url in found_results:
                    f.write(f"{platform}: {url}\n")
            else:
                f.write("No results found.\n")
        print(f"{purple}[INFO]{white} Results saved to {filepath}{reset}")
    except Exception as e:
        print(f"{purple}[ERROR]{white} Failed to save results: {e}{reset}")
        return
    completion_message("Username Lookup completed its operations")
def main():
    try:
        username_lookup()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[RETURN]{white} Press Enter to continue...{reset}")

if __name__ == "__main__":
    main()