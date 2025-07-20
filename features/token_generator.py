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
    print(f"{purple}┌───────────────[ {white}AirFlow - TOKEN GENERATOR{purple} ]───────────────┐{reset}")
    print(f"{purple}│{white} {prompt:<50} {reset}")
    print(f"{purple}│{white} >> {reset}", end="")
    user_input = input()
    print(f"{purple}└──────────────────────────────────────────────────┘{reset}")
    return user_input.strip()
def status_message(message):
    print(f"{purple}[EXECUTING]{white} {message}...{reset}")
def completion_message(message):
    print(f"{purple}[COMPLETE]{white} {message}{reset}")
def generate_token():
    base64_chars = string.ascii_letters + string.digits + "-_"
    second_part_chars = string.ascii_letters + string.digits
    third_part_chars = string.ascii_letters + string.digits + "-_"
    first_part = ''.join(random.choice(base64_chars) for _ in range(27))
    second_part = ''.join(random.choice(second_part_chars) for _ in range(6))
    third_part = ''.join(random.choice(third_part_chars) for _ in range(27))
    token = f"{first_part}.{second_part}.{third_part}"
    return token
def token_generator():
    num_tokens = styled_input("Enter the number of tokens to generate:")
    try:
        num_tokens = int(num_tokens)
        if num_tokens <= 0:
            raise ValueError
    except ValueError:
        print(f"{purple}[ERROR]{white} Invalid number of tokens. Must be a positive integer.{reset}")
        return
    status_message(f"Generating {num_tokens} Discord-like tokens")
    tokens = []
    for i in range(num_tokens):
        token = generate_token()
        tokens.append(token)
        print(f"{purple}[INFO]{white} Generated token {i+1}/{num_tokens}: {token}{reset}")
        time.sleep(0.1)
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"tokens_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("Generated Discord-like Tokens\n")
            f.write("=" * 30 + "\n\n")
            for i, token in enumerate(tokens, 1):
                f.write(f"Token {i}: {token}\n")
        print(f"{purple}[INFO]{white} Tokens saved to {filepath}{reset}")
    except Exception as e:
        print(f"{purple}[ERROR]{white} Failed to save tokens: {e}{reset}")
        return
    completion_message("Token Generator completed its operations")
def main():
    try:
        token_generator()
    except Exception as e:
        print(f"{purple}[ERROR]{white} An unexpected error occurred: {e}{reset}")
    finally:
        input(f"{purple}[RETURN]{white} Press Enter to continue...{reset}")

if __name__ == "__main__":
    main()