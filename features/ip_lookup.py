import requests
import time
from colorama import init, Fore, Style
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - IP LOOKUP{purple} ]───────────────┐{reset}")
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
        headers = {"User-Agent": "Ruin-IP-Lookup/1.0"}
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
def ip_lookup():
    ip_address = styled_input("Enter the IP address to look up:")
    if not ip_address:
        print(f"{purple}[ERROR]{white} No IP address provided. Exiting...{reset}")
        return
    status_message(f"Looking up IP address: {ip_address}")
    url = f"http://ip-api.com/json/{ip_address}"
    response = make_request_with_retry("GET", url)
    if not response or response.status_code != 200:
        print(f"{purple}[ERROR]{white} Failed to fetch IP info: Status {response.status_code if response else 'No response'}, Response: {response.text if response else 'None'}{reset}")
        return
    try:
        ip_info = response.json()
        if ip_info.get("status") != "success":
            print(f"{purple}[ERROR]{white} Failed to fetch IP info: {ip_info.get('message', 'Unknown error')}{reset}")
            return
        country = ip_info.get("country", "Not provided")
        region = ip_info.get("regionName", "Not provided")
        city = ip_info.get("city", "Not provided")
        zip_code = ip_info.get("zip", "Not provided")
        latitude = ip_info.get("lat", "Not provided")
        longitude = ip_info.get("lon", "Not provided")
        timezone = ip_info.get("timezone", "Not provided")
        isp = ip_info.get("isp", "Not provided")
        org = ip_info.get("org", "Not provided")
        as_name = ip_info.get("as", "Not provided")
        proxy = ip_info.get("proxy", False)
        hosting = ip_info.get("hosting", False)
        print(f"{purple}[INFO]{white} IP Lookup Results for {ip_address}:{reset}")
        print(f"  - Country: {white}{country}{reset}")
        print(f"  - Region: {white}{region}{reset}")
        print(f"  - City: {white}{city}{reset}")
        print(f"  - ZIP Code: {white}{zip_code}{reset}")
        print(f"  - Latitude: {white}{latitude}{reset}")
        print(f"  - Longitude: {white}{longitude}{reset}")
        print(f"  - Timezone: {white}{timezone}{reset}")
        print(f"  - ISP: {white}{isp}{reset}")
        print(f"  - Organization: {white}{org}{reset}")
        print(f"  - AS: {white}{as_name}{reset}")
        print(f"  - Proxy/VPN: {white}{proxy}{reset}")
        print(f"  - Hosting: {white}{hosting}{reset}")
    except ValueError:
        print(f"{purple}[ERROR]{white} Failed to parse IP info response: {response.text}{reset}")
        return
    completion_message("IP Lookup completed its operations")
def main():
    try:
        ip_lookup()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[RETURN]{white} Press Enter to continue...{reset}")

if __name__ == "__main__":
    main()