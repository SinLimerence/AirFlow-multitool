import time
from colorama import init, Fore, Style
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - PHONE NUMBER LOOKUP{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")  
    user_input = input()  
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def phone_number_lookup():
    phone_number = styled_input("Enter the phone number (with country code, e.g., +12025550123):")
    if not phone_number:
        print(f"{purple}[ERROR]{white} No phone number provided. Exiting...{reset}")
        return
    status_message(f"Looking up phone number: {phone_number}")
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"{purple}[ERROR]{white} Invalid phone number format. Please include the country code (e.g., +12025550123).{reset}")
            return
        operator = carrier.name_for_number(parsed_number, "en") or "Not provided"
        line_type = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Landline"
        country = phonenumbers.region_code_for_number(parsed_number) or "Not provided"
        region = geocoder.description_for_number(parsed_number, "en") or "Not provided"
        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_info = timezones[0] if timezones else "Not provided"
        print(f"{purple}[INFO]{white} Phone Number Lookup Results for {phone_number}:{reset}")
        print(f"  - Country: {white}{country}{reset}")
        print(f"  - Region: {white}{region}{reset}")
        print(f"  - Operator: {white}{operator}{reset}")
        print(f"  - Line Type: {white}{line_type}{reset}")
        print(f"  - Timezone: {white}{timezone_info}{reset}")

    except phonenumbers.NumberParseException as e:
        print(f"{purple}[ERROR]{white} Failed to parse phone number: {e}{reset}")
        return
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
        return
    completion_message("Phone Number Lookup completed its operations")
def main():
    try:
        phone_number_lookup()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[RETURN]{white} Press Enter to continue...{reset}")

if __name__ == "__main__":
    main()