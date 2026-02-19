import subprocess

def run_spiderfoot(target):
    command = ["spiderfoot", "-s", target, "-m", "all"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running SpiderFoot: {e}"