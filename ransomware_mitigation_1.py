import socket
import os
import struct
from datetime import datetime

LOG_FILE = "mitigation_report.txt"
INTERFACE = "enp0s3"
SCORE_THRESHOLD = 5

threat_scores = {}


def recovery_alert(attacker_ip, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] THREAT ISOLATED | IP: {attacker_ip} | Action: {action}\n")
    print(f"\nPhase 4: Recovery Alert Saved! Threat from {attacker_ip} is documented.")


def dynamic_port_shutdown(attacker_ip):
    print(f"\nPhase 3: THREAT SCORE CRITICAL ({SCORE_THRESHOLD}/{SCORE_THRESHOLD})")
    print(f"Executing Simulation: Disabling network interface {INTERFACE}...")

    os.system(f"sudo ip link set {INTERFACE} down")

    action = f"Interface {INTERFACE} disabled via ip link set down"
    print(f"SUCCESS: {action}")

    recovery_alert(attacker_ip, action)


def monitor_traffic():
    print("Phase 1: Traffic Monitoring Started via Raw Sockets...")

    try:
        conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    except Exception as e:
        print(f"Error creating socket (Make sure to run with sudo): {e}")
        return

    while True:
        raw_data, addr = conn.recvfrom(65535)

        eth_header = raw_data[0:14]
        eth = struct.unpack('!6s6sH', eth_header)
        eth_protocol = socket.htons(eth[2])

        if eth_protocol == 8:
            ip_header = raw_data[14:34]
            iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

            source_ip = socket.inet_ntoa(iph[8])
            dest_ip = socket.inet_ntoa(iph[9])

            if source_ip == "192.168.1.11":
                continue

            if source_ip:
                threat_scores[source_ip] = threat_scores.get(source_ip, 0) + 1
                score = threat_scores[source_ip]

                print(f"Detection: Packet from {source_ip} | Score: {score}")

                if score >= SCORE_THRESHOLD:
                    dynamic_port_shutdown(source_ip)
                    break


if __name__ == "__main__":
    monitor_traffic()