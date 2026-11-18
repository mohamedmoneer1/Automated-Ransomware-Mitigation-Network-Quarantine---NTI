# Automated Ransomware Mitigation & Network Quarantine

## 📌 Project Overview
This project is an automated, host-based network quarantine system developed as part of the **National Telecommunication Institute (NTI)** training program. It is designed to detect suspicious network activity, calculate threat scores in real-time, and automatically isolate the targeted machine to prevent the spread of ransomware or lateral movement within a network.

## 🏗️ Architecture & Topology
The project was tested and implemented using a **Virtual Machine (VM) environment**:
* **Attacker VM:** Simulates malicious activity and network scanning.
* **Defender VM (Linux):** Runs the mitigation script to monitor traffic and enforce quarantine.

## ✨ Key Features
* **Agentless Monitoring:** Uses Python Raw Sockets to inspect network traffic without relying on external IDS tools like Snort.
* **Dynamic Threat Scoring:** Tracks the frequency of packets from incoming IP addresses.
* **Automated Quarantine:** Instantly disables the host's network interface (e.g., `enp0s3`) once the threat score exceeds the defined threshold.
* **Incident Logging:** Documents the attacker's IP, timestamp, and mitigation action in a local log file (`mitigation_report.txt`).

## ⚙️ How It Works
1. **Phase 1 (Traffic Monitoring):** Captures incoming packets at the Ethernet layer.
2. **Phase 2 (Scoring):** Extracts the source IP and increments its threat score.
3. **Phase 3 (Isolation):** If an IP reaches the critical threshold (Score: 5), the system executes a system-level command (`sudo ip link set down`) to cut off network access.
4. **Phase 4 (Recovery Alert):** Logs the incident for further forensic analysis.

## 🚀 Usage & Execution
To run the mitigation script, you need a Linux environment and `root` privileges (required for raw sockets and interface management).

```bash
# Clone the repository
git clone [https://github.com/mohamedmoneer1/Automated-Ransomware-Mitigation-Network-Quarantine---NTI.git](https://github.com/mohamedmoneer1/Automated-Ransomware-Mitigation-Network-Quarantine---NTI.git)

# Navigate to the directory
cd Automated-Ransomware-Mitigation-Network-Quarantine---NTI

# Run the script with sudo
sudo python3 ransomware_mitigation_1.py
```
## 📂 Repository Contents
* `ransomware_mitigation_1.py`: The main Python mitigation script.
* `Automated Ransomware Mitigation.pdf`: Comprehensive project report.
* `Automated Ransomware Mitigation & Network Quarantine.pptx`: Presentation slides.
* `Screenshots`: Terminal execution and successful threat blocking evidence.
