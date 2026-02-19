import argparse

def run_tool(tool, target):
    if tool == "harvester":
        import Harvester
        Harvester.run_theharvester(target)
    elif tool == "reconng":
        import ReconNG
        ReconNG.run_reconng(target)
    elif tool == "spiderfoot":
        import SpiderFoot
        SpiderFoot.run_spiderfoot(target)
    elif tool == "maltego":
        import Maltego
        Maltego.run_maltego(target)
    elif tool == "sherlock":
        import Sherlock
        Sherlock.run_sherlock(target)
    elif tool == "foca":
        import FOCA
        FOCA.run_foca(target)
    else:
        print("Unknown tool.")

def main():
    parser = argparse.ArgumentParser(description="OSINT Tool Selector")
    parser.add_argument("tool", choices=["harvester", "reconng", "spiderfoot", "maltego", "sherlock", "foca"], help="Tool to run")
    parser.add_argument("target", help="Target to investigate")
    args = parser.parse_args()
    run_tool(args.tool, args.target)

if __name__ == "__main__":
    main()