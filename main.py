import socket
from datetime import datetime

# Definisi Warna Neon Hacker
G_LIGHT = "\033[92m" # Hijau Terang
G_DARK = "\033[32m"  # Hijau Gelap
RESET = "\033[0m"
BOLD = "\033[1m"

def print_banner():
    # ASCII Art GhostKnock dengan tema hantu digital
    banner = f"""
{G_LIGHT}
          .-.
         ( " )  {G_DARK}<-- GhostKnock is watching...{G_LIGHT}
          ^v^

  _______ _                 _   _  __                 _    
 | ______| |__   ___  ___ _| |_| |/ /_ __   ___   ___| | __
 | |  _  | '_ \ / _ \/ __|_   _| ' /| '_ \ / _ \ / __| |/ /
 | |_| | | | | | (_) \__ \ | | | . \| | | | (_) | (__|   < 
  \____/ |_| |_|\___/|___/ |_| |_|\_\_| |_|\___/ \___|_|\_\\
                                                            
      {BOLD}>> SILENT NETWORK PROBE | VERSION 1.0 <<{RESET}{G_DARK}
    [ Target your doors, knock without a trace ]
{RESET}
    """
    print(banner)

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        
        # connect_ex mengembalikan 0 jika koneksi sukses
        result = s.connect_ex((ip, port))
        
        services = {
            21: "FTP", 22: "SSH", 23: "TELNET", 25: "SMTP", 
            53: "DNS", 80: "HTTP", 443: "HTTPS", 3306: "MySQL", 
            8080: "HTTP-PROXY"
        }
        
        service_name = services.get(port, "Unknown Service")
        
        if result == 0:
            print(f"{G_LIGHT}[+] PORT {port:<5} | [ OPEN ]   | {service_name}{RESET}")
        else:
            # Opsional: buka baris di bawah jika ingin melihat port yang tertutup
            # print(f"{G_DARK}[-] PORT {port:<5} | [CLOSED]{RESET}")
            pass
            
        s.close()
    except KeyboardInterrupt:
        print(f"\n{G_LIGHT}[!] Sinyal berhenti diterima. Menghilang...{RESET}")
        exit()
    except:
        pass

# --- MAIN ---
print_banner()

target = input(f"{G_LIGHT}ghost@knock:~# {RESET}Masukkan IP Target: ")

print(f"\n{G_DARK}" + "—" * 60)
print(f"{G_LIGHT}[*] Memulai pemindaian pada: {target}")
print(f"[*] Waktu deteksi: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"{G_DARK}" + "—" * 60 + f"{RESET}")

# Daftar port yang akan diperiksa
common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5900, 8080]

print(f"{G_LIGHT}{'PORT':<10} | {'STATUS':<10} | {'SERVICE'}{RESET}")
print(f"{G_DARK}" + "-" * 60 + f"{RESET}")

for port in common_ports:
    scan_port(target, port)

print(f"{G_DARK}" + "—" * 60)
print(f"{G_LIGHT}[!] GhostKnock selesai. Kembali ke kegelapan.{RESET}\n")