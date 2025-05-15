# CrackXP - WiFi Security Tool
## By Laila19 | GitHub: lailacypher

### 📥 Installation Guide
Requirements
Linux OS (Kali Linux recommended)
Python 3.x
Wireless Tools: aircrack-ng, hashcat, iwconfig
Root privileges

### Step-by-Step Installation

Clone the Repository

```bash
git clone https://github.com/lailacypher/CrackXP.git
cd CrackXP
```
Install Dependencies

```bash
sudo apt update && sudo apt install -y aircrack-ng hashcat python3
```
Make the Script Executable

```bash
chmod +x crackxp.py
````
Run CrackXP

```bash
sudo python3 crackxp.py
```

### 🛠 Usage Tutorial

1. Enable Monitor Mode
Select Option 1

Enter your wireless interface (e.g., wlan0)

This puts your WiFi card in monitor mode for packet capture.

2. Capture WiFi Signals
Select Option 2

Scans and lists nearby WiFi networks.

3. Capture Handshake (Besside-ng or Airodump-ng)
Option 3 (Besside-ng) – Automates handshake capture.

Option 4 (Airodump-ng) – Manual targeting with BSSID/Channel selection.

Captured handshakes are saved in /root/Desktop/handshake/.

4. Crack WPA2-PSK Passwords
Option 5 (Aircrack-ng) – Fast brute-force with wordlists.

Option 6 (Hashcat) – GPU-accelerated cracking (requires compatible GPU).

5. Disable Monitor Mode
Option 7 – Reverts your WiFi card to managed mode.

### 🔹 Example Workflow
bash
1. sudo python3 crackxp.py  
2. Select [1] → Enter interface (wlan0)  
3. Select [2] → Find target network  
4. Select [4] → Enter BSSID & Channel  
5. Wait for handshake capture  
6. Select [5] → Run Aircrack with a wordlist  
7. Recover password (if weak)  
8. Select [7] → Disable monitor mode  
📌 Notes
Wordlists recommended: rockyou.txt, SecLists

For Hashcat: Use hashcat -m 2500 for WPA2 cracking.
