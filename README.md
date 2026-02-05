# GhostKnock - Silent Network Probe

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-red.svg)

GhostKnock is a lightweight, stealthy port scanner designed for network reconnaissance. It silently probes target systems for open ports, providing detailed service identification and a clean, terminal-based interface.

## Features

- **Stealthy Scanning**: Minimal network footprint with configurable timeouts
- **Service Detection**: Identifies common services running on open ports
- **Customizable Configuration**: JSON-based settings for ports, colors, and timeouts
- **Real-time Output**: Live display of scan results with color-coded formatting
- **Keyboard Interrupt Handling**: Graceful exit on user interruption
- **Cross-platform**: Works on Windows, macOS, and Linux

## Supported Ports

The scanner checks the following common ports by default:

| Port | Service    | Port | Service |
| ---- | ---------- | ---- | ------- |
| 21   | FTP        | 110  | POP3    |
| 22   | SSH        | 139  | NetBIOS |
| 23   | TELNET     | 143  | IMAP    |
| 25   | SMTP       | 443  | HTTPS   |
| 53   | DNS        | 445  | SMB     |
| 80   | HTTP       | 3306 | MySQL   |
| 3389 | RDP        | 5900 | VNC     |
| 8080 | HTTP-PROXY |      |         |

## Installation

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses built-in `socket` and `json` modules)

### Setup

1. Clone or download the project files:

   ```bash
   git clone https://github.com/jodijonatan/ghostknock.git
   cd ghostknock
   ```

2. Ensure `config.json` and `main.py` are in the same directory.

## Usage

### Basic Scanning

Run the scanner and enter a target IP address when prompted:

```bash
python main.py
```

Example output:

```
          .-.
         ( " )  <-- GhostKnock is watching...
          ^v^

  _______ _                 _   _  __                 _
 | ______| |__   ___  ___ _| |_| |/ /_ __   ___   ___| | __
 | |  _  | '_ \ / _ \/ __|_   _| ' /| '_ \ / _ \ / __| |/ /
 | |_| | | | | | (_) \__ \ | | | . \| | | | (_) | (__|   <
  \____/ |_| |_|\___/|___/ |_| |_|\_\_| |_|\___/ \___|_|\_\\

      >> SILENT NETWORK PROBE | VERSION 1.0 <<
    [ Target your doors, knock without a trace ]

ghost@knock:~# Enter Target IP: 192.168.1.1

------------------------------------------------------------
[*] Starting scan on: 192.168.1.1
[*] Detection time: 2023-12-07 14:30:45
------------------------------------------------------------
PORT    | STATUS    | SERVICE
------------------------------------------------------------
[+] PORT 22    | [ OPEN ]   | SSH
[+] PORT 80    | [ OPEN ]   | HTTP
[+] PORT 443   | [ OPEN ]   | HTTPS
------------------------------------------------------------
[!] GhostKnock finished. Returning to the shadows.
```

### Configuration

Customize the scanner behavior by editing `config.json`:

```json
{
  "settings": {
    "timeout": 2.0,
    "targets": [
      21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5900, 8080
    ]
  },
  "colors": {
    "primary": "\u001b[92m",
    "secondary": "\u001b[32m",
    "reset": "\u001b[0m"
  }
}
```

- `timeout`: Connection timeout in seconds (default: 2.0)
- `targets`: List of ports to scan
- `colors`: ANSI color codes for terminal output

## Ethical Usage

**⚠️ WARNING**: This tool is intended for educational and authorized security testing purposes only. Unauthorized scanning of networks or systems may violate laws and regulations. Always obtain explicit permission before scanning any target.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

The authors are not responsible for any misuse of this tool. Use at your own risk and ensure compliance with applicable laws and regulations.

---

**"Target your doors, knock without a trace."**
