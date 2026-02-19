import subprocess

def run_reconng(target, module="recon/domains-hosts/google_site", command="run"):
    """
    Run Recon-ng with a specified module and command.
    :param target: The domain or IP to investigate.
    :param module: Recon-ng module to use.
    :param command: Command to execute in Recon-ng.
    :return: Output from Recon-ng.
    """
    recon_commands = f"""
    workspace osint_workspace
    add domains {target}
    use {module}
    {command}
    exit
    """
    try:
        result = subprocess.run(
            ["recon-ng", "-r", "-"],
            input=recon_commands,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running Recon-ng: {e}"

# Example modules you can use:
# - recon/domains-hosts/google_site
# - recon/domains-hosts/bing_domain_web
# - recon/domains-contacts/whois_pocs
# - recon/domains-contacts/whois