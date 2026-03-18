import subprocess


def run_git_command(command):
    try:
        return subprocess.check_output(command, shell=True).decode().strip()
    except:
        return ""


def is_git_repo():
    try:
        output = run_git_command("git rev-parse --is-inside-work-tree")
        return output == "true"
    except:
        return False


def suggest(last_cmd):
    last_cmd = last_cmd.strip()

    # ❌ Not a git repository
    if not is_git_repo():
        return (
            "git init",
            "This is not a git repository. Initialize it first."
        )

    status = run_git_command("git status --porcelain")
    branch = run_git_command("git branch --show-current")

    staged = []
    unstaged = []

    for line in status.splitlines():
        if line.startswith("A") or line.startswith("M"):
            staged.append(line)
        elif line.startswith(" M"):
            unstaged.append(line)

    # ❌ Trying to commit without staging
    if "git commit" in last_cmd and not staged:
        return (
            "git add .",
            "You tried to commit but nothing is staged."
        )

    # ❌ Trying to push without commit
    if "git push" in last_cmd and status:
        return (
            "git commit -m 'your message'",
            "You have uncommitted changes. Commit first."
        )

    # ✅ If staged changes exist
    if staged:
        return (
            "git commit -m 'your message'",
            "You have staged changes ready to commit."
        )

    # ⚠️ If only unstaged changes
    elif unstaged:
        return (
            "git add .",
            "You have unstaged changes. Add them first."
        )

    # 🚀 After commit → suggest push
    elif "git commit" in last_cmd:
        return (
            f"git push origin {branch}",
            f"Push your commits to '{branch}'."
        )

    # 🧠 Default fallback
    else:
        return (
            "git status",
            "Check your repository state."
        )