# OSINT Toolkit for Linux

This toolkit lets you run multiple OSINT tools (theHarvester, Recon-ng, SpiderFoot, Sherlock) from a simple web interface.  
Everything is ready to install and use on a Linux machine.

## Features

- Easy web interface for selecting tools and targets
- Automated setup and installation
- Supports theHarvester, Recon-ng, SpiderFoot, Sherlock

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Osint.git
cd Osint
```

### 2. Run the Setup Script

This installs all required tools and Python dependencies.

```bash
chmod +x setup.sh
./setup.sh
```

### 3. Start the Web App

```bash
python3 app.py
```

### 4. Use the Toolkit

- Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Select a tool, enter your target, and run your search

## Tools Included

- **theHarvester**: Finds emails, subdomains, hosts, and IPs
- **Recon-ng**: Modular framework for domain and contact reconnaissance
- **SpiderFoot**: Automated OSINT scanning
- **Sherlock**: Finds usernames across social networks

## Troubleshooting

- Make sure you run the setup script as root (with `sudo`) if you get permission errors.
- All tools must be installed and accessible from the command line.
- If you have issues, check the output in your terminal for error messages.

## License

MIT License

---

**Enjoy your OSINT toolkit!**
