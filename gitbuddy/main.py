import subprocess
from gitbuddy.suggester import suggest
from colorama import Fore, Style, init
init(autoreset=True)
def get_last_command():
    try:
        return input("👉 What did you run last? ")
    except:
        return ""

def main():
    last_cmd = get_last_command()

    suggestion, reason = suggest(last_cmd)

    print("\n" + "="*40)
    print(Fore.CYAN + "🧠 Last command: " + Style.RESET_ALL + last_cmd)
    print(Fore.GREEN + "👉 Suggested: " + Style.RESET_ALL + suggestion)
    print(Fore.YELLOW + "💡 Why: " + Style.RESET_ALL + reason)
    print("="*40 + "\n")
if __name__ == "__main__":
    main()