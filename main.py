import socket
import json
from datetime import datetime

# --- LOAD KONFIGURASI DARI JSON ---
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Error: File config.json tidak ditemukan!")
    exit()

# Mapping warna dari config
G_LIGHT = config['colors']['primary']
G_DARK = config['colors']['secondary']
RESET = config['colors']['reset']
BOLD = "\033[1m"
TIMEOUT = config['settings']['timeout']
COMMON_PORTS = config['settings']['targets']

def print_banner():
    banner = rf"""
{G_LIGHT}
          .-.
         ( " )  {G_DARK}<-- GhostKnock is watching...{G_LIGHT}
          ^v^

  _______ _                 _   _  __                 _
 | ______| |__   ___  ___ _| |_| |/ /_ __   ___   ___| | __
 | |  _  | '_ \ / _ \/ __|_   _| ' /| '_ \ / _ \ / __| |/ /
 | |_| | | | | | (_) \__ \ | | | . \| | | | (_) | (__|   < 
  \____/ |_| |_|\___/|___/ |_| |_|\_\_| |_|\___/ \___|_|\_\\

      {BOLD}>> SILENT NETWORK PROBE | VERSION 1.1 <<{RESET}{G_DARK}
    [ Target your doors, knock without a trace ]
{RESET}
    """
    print(banner)

def get_banner(s):
    """Mencoba mengambil string banner dari socket yang terbuka"""
    try:
        # Mengirim data kosong (atau enter) untuk memancing respon dari server
        return s.recv(1024).decode().strip('\n').strip('\r')
    except:
        return "No Banner"

def scan_port(ip, port):
    try:
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.settimeout(TIMEOUT)

        target_ip = socket.gethostbyname(ip) 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)

        result = s.connect_ex((target_ip, port))

        services = {
            21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 139: "NetBIOS", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP", 5900: "VNC",
            8080: "HTTP-PROXY"
        }

        service_name = services.get(port, "Unknown")

        if result == 0:
            # Mencoba mendapatkan informasi versi (Banner)
            banner_info = get_banner(s)
            
            # Jika HTTP, biasanya butuh request manual untuk dapat banner, 
            # ini adalah implementasi sederhana untuk layanan berbasis teks (SSH/FTP/SMTP)
            print(f"{G_LIGHT}[+] PORT {port:<5} | [ OPEN ]   | {service_name:<12} | {banner_info}{RESET}")
            s.close()
            return True

        s.close()
        return False
    except KeyboardInterrupt:
        print(f"\n{G_LIGHT}[!] Sinyal berhenti diterima. Menghilang...{RESET}")
        exit()
    except:
        return False

# --- MAIN ---
print_banner()

target = input(f"{G_LIGHT}ghost@knock:~# {RESET}Masukkan IP Target: ")

print(f"\n{G_DARK}" + "—" * 80)
print(f"{G_LIGHT}[*] Memulai pemindaian pada: {target}")
print(f"[*] Waktu deteksi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{G_DARK}" + "—" * 80 + f"{RESET}")

# Header tabel diperlebar untuk menampung banner
print(f"{G_LIGHT}{'PORT':<10} | {'STATUS':<10} | {'SERVICE':<12} | {'VERSION/BANNER'}{RESET}")
print(f"{G_DARK}" + "-" * 80 + f"{RESET}")

port_found = 0

for port in COMMON_PORTS:
    if scan_port(target, port):
        port_found += 1

if port_found == 0:
    print(f"{G_DARK}[-] Tidak ada port terbuka yang ditemukan pada target ini.{RESET}")

print(f"{G_DARK}" + "—" * 80)
print(f"{G_LIGHT}[!] GhostKnock selesai. Kembali ke kegelapan.{RESET}\n")