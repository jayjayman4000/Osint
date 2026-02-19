from flask import Flask, render_template, request
import Harvester, ReconNG, SpiderFoot, Maltego, Sherlock, FOCA

app = Flask(__name__)

TOOLS = {
    "harvester": Harvester.run_theharvester,
    "reconng": ReconNG.run_reconng,
    "spiderfoot": SpiderFoot.run_spiderfoot,
    "maltego": Maltego.run_maltego,
    "sherlock": Sherlock.run_sherlock,
    "foca": FOCA.run_foca,
}

RECONNG_MODULES = [
    "recon/domains-hosts/google_site",
    "recon/domains-hosts/bing_domain_web",
    "recon/domains-contacts/whois_pocs",
    "recon/domains-contacts/whois"
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    selected_tool = None
    reconng_module = RECONNG_MODULES[0]
    reconng_command = "run"
    if request.method == "POST":
        selected_tool = request.form["tool"]
        target = request.form["target"]
        if selected_tool == "reconng":
            reconng_module = request.form.get("reconng_module", reconng_module)
            reconng_command = request.form.get("reconng_command", reconng_command)
            result = ReconNG.run_reconng(target, reconng_module, reconng_command)
        else:
            func = TOOLS.get(selected_tool)
            if func:
                result = func(target)
            else:
                result = "Unknown tool selected."
    return render_template(
        "index.html",
        tools=TOOLS.keys(),
        result=result,
        selected_tool=selected_tool,
        reconng_modules=RECONNG_MODULES,
        reconng_module=reconng_module,
        reconng_command=reconng_command
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)