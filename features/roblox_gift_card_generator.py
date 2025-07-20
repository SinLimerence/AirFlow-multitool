import os
import time
import random
import string
from datetime import datetime
from colorama import init, Fore, Style
init()
purple = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL
def styled_input(prompt):
    print(f"{purple}┌───────────────[ {white}AirFlow - ROBLOX GIFT CARD GENERATOR{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")  # Place the input prompt inside the box
    user_input = input()  # Capture input on the same line
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def generate_gift_card_code():
    code_chars = string.digits  # 0-9
    code = ''.join(random.choice(code_chars) for _ in range(16))
    formatted_code = f"{code[:4]}-{code[4:8]}-{code[8:12]}-{code[12:]}"
    return formatted_code
def roblox_gift_card_generator():
    num_codes = styled_input("Enter the number of Roblox gift card codes to generate:")
    try:
        num_codes = int(num_codes)
        if num_codes <= 0:
            raise ValueError
    except ValueError:
        print(f"{purple}[ERROR]{white} Invalid number of gift card codes. Must be a positive integer.{reset}")
        return
    status_message(f"Generating {num_codes} Roblox gift card codes")
    gift_codes = []
    for i in range(num_codes):
        gift_code = generate_gift_card_code()
        gift_codes.append(gift_code)
        print(f"{purple}[INFO]{white} Generated gift card code {i+1}/{num_codes}: {gift_code}{reset}")
        time.sleep(0.1)  
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"roblox_gift_codes_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("Generated Roblox Gift Card Codes\n")
            f.write("=" * 32 + "\n\n")
            for i, code in enumerate(gift_codes, 1):
                f.write(f"Gift Card Code {i}: {code}\n")
        print(f"{purple}[INFO]{white} Gift card codes saved to {filepath}{reset}")
    except Exception as e:
        print(f"{purple}[ERROR]{white} Failed to save gift card codes: {e}{reset}")
        return
    completion_message("Roblox Gift Card Generator completed its operations")
def main():
    try:
        roblox_gift_card_generator()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[RETURN]{white} Press Enter to continue...{reset}")

if __name__ == "__main__":
    main()