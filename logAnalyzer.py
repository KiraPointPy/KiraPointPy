import re
import os
from collections import Counter


def analyze_security_logs():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "access.log")

    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    if not os.path.exists(file_path):
        print("ERROR: File not found at:")
        print(file_path)
        return

    with open(file_path, 'r') as file:
        log_data = file.read()

    ip_addresses = re.findall(ip_pattern, log_data)
    ip_counts = Counter(ip_addresses)

    print("--- ENTERPRISE LOG ANALYZER ---")
    print(f"Total connections tracked: {len(ip_addresses)}")
    print("-" * 40)

    threat_found = False
    for ip, count in ip_counts.items():
        if count > 3:
            print(f"[ALERT] IP: {ip} - {count} failed attempts!")
            threat_found = True

    if not threat_found:
        print("[INFO] System secure. No threats detected.")

    print("-" * 40)


if __name__ == "__main__":
    analyze_security_logs()