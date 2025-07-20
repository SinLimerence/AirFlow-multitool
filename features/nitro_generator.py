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
    print(f"{purple}┌───────────────[ {white}AirFlow - NITRO GENERATOR{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")  # Place the input prompt inside the box
    user_input = input()  # Capture input on the same line
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def generate_nitro_link():
    base_url = "https://discord.gift/"
    code_chars = string.ascii_letters  # a-z and A-Z
    gift_code = ''.join(random.choice(code_chars) for _ in range(24))
    nitro_link = f"{base_url}{gift_code}"
    return nitro_link
def nitro_generator():
    num_links = styled_input("Enter the number of Nitro gift links to generate:")
    try:
        num_links = int(num_links)
        if num_links <= 0:
            raise ValueError
    except ValueError:
        print(f"{purple}[ERROR]{white} Invalid number of gift links. Must be a positive integer.{reset}")
        return
    status_message(f"Generating {num_links} Discord Nitro gift links")
    gift_links = []
    for i in range(num_links):
        gift_link = generate_nitro_link()
        gift_links.append(gift_link)
        print(f"{purple}[INFO]{white} Generated gift link {i+1}/{num_links}: {gift_link}{reset}")
        time.sleep(0.1)  
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"nitro_gifts_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("Generated Discord Nitro Gift Links\n")
            f.write("=" * 35 + "\n\n")
            for i, link in enumerate(gift_links, 1):
                f.write(f"Gift Link {i}: {link}\n")
        print(f"{purple}[INFO]{white} Gift links saved to {filepath}{reset}")
    except Exception as e:
        print(f"{purple}[ERROR]{white} Failed to save gift links: {e}{reset}")
        return
    completion_message("Nitro Generator completed its operations")
def main():
    try:
        nitro_generator()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[RETURN]{white} Press Enter to continue...{reset}")

if __name__ == "__main__":
    main()