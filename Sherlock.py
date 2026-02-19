import subprocess
import os

def run_sherlock(target):
    sherlock_path = os.path.join(os.getcwd(), "sherlock", "sherlock.py")
    command = ["python3", sherlock_path, target]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running Sherlock: {e}"