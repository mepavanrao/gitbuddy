import subprocess
from gitbuddy.suggester import suggest

def get_last_command():
    try:
        cmd = subprocess.check_output(
            'powershell "Get-History | Select-Object -Last 1 | ForEach-Object {$_.CommandLine}"',
            shell=True
        )
        return cmd.decode().strip()
    except:
        return "No history found"

def main():
    last_cmd = get_last_command()

    suggestion, reason = suggest(last_cmd)

    print("\n🧠 Last command:", last_cmd)
    print("👉 Suggested:", suggestion)
    print("💡 Why:", reason, "\n")

if __name__ == "__main__":
    main()