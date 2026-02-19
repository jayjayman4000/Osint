import argparse
import subprocess

def run_theharvester(target):
    command = ["theharvester", "-d", target, "-b", "all"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running theHarvester: {e}"

def main():
    parser = argparse.ArgumentParser(description="Run theHarvester OSINT tool")
    parser.add_argument("target", help="Target domain, IP, or email")
    args = parser.parse_args()
    print(run_theharvester(args.target))

if __name__ == "__main__":
    main()


