import requests
import time
from colorama import init, Fore, Style
import os
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - EMAIL LOOKUP{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def make_request_with_retry(url, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 429:
                retry_after = float(response.headers.get("Retry-After", 2))
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
def email_lookup():
    email = styled_input("Enter the email address to look up:")
    if not email:
        print(f"{purple}[ERROR]{white} No email address provided. Exiting...{reset}")
        return
    status_message(f"Looking up email: {email}")
    url = f"https://leakcheck.io/api/public?check={email}"
    response = make_request_with_retry(url)
    if not response:
        print(f"{purple}[ERROR]{white} Failed to query the LeakCheck API after multiple attempts.{reset}")
        return
    if response.status_code == 200:
        try:
            data = response.json()
            if data.get("success", False):
                found = data.get("found", 0)
                sources = data.get("sources", [])
                if found > 0 and sources:
                    print(f"{purple}[INFO]{white} Email found in the following breaches:{reset}")
                    for source in sources:
                        breach_name = source.get("name", "Unknown")
                        breach_date = source.get("date", "Unknown") or "Unknown"
                        print(f"  - {white}{breach_name}{reset} (Breached on: {breach_date})")
                else:
                    print(f"{purple}[INFO]{white} No breaches found for this email.{reset}")
            else:
                print(f"{purple}[ERROR]{white} LeakCheck API returned an error: {data.get('error', 'Unknown error')}{reset}")
        except ValueError:
            print(f"{purple}[ERROR]{white} Failed to parse LeakCheck API response: {response.text}{reset}")
    else:
        print(f"{purple}[ERROR]{white} Failed to query the LeakCheck API: Status {response.status_code}, Response: {response.text}{reset}")
    completion_message("Email Lookup completed its operations")
def main():
    try:
        email_lookup()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()