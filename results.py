import csv
from collections import Counter
from datetime import datetime

INPUT_FILE = "pentest_results.csv"
OUTPUT_FILE = "pentest_report.txt"

events = []
ips = Counter()
user_agents = Counter()
timestamps = []

with open(INPUT_FILE, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        events.append(row)
        ips[row['source_ip']] += 1
        user_agents[row['user_agent']] += 1
        timestamps.append(row['timestamp'])

total_events = len(events)

first_seen = min(timestamps) if timestamps else "N/A"
last_seen = max(timestamps) if timestamps else "N/A"

with open(OUTPUT_FILE, "w") as report:
    report.write("=== PENTEST ENGAGEMENT REPORT ===\n")
    report.write(f"Generated: {datetime.utcnow().isoformat()} UTC\n\n")

    report.write("== Engagement Summary ==\n")
    report.write(f"Total form submissions: {total_events}\n")
    report.write(f"First activity: {first_seen}\n")
    report.write(f"Last activity:  {last_seen}\n\n")

    report.write("== Top Source IPs ==\n")
    for ip, count in ips.most_common(10):
        report.write(f"{ip}: {count} submissions\n")
    report.write("\n")

    report.write("== User-Agent Breakdown ==\n")
    for ua, count in user_agents.most_common(10):
        report.write(f"{count}x {ua}\n")
    report.write("\n")

    report.write("== Assessment ==\n")
    report.write(
        "The application accepted credential-form submissions without technical controls\n"
        "to prevent misuse. This confirms exposure to credential harvesting attacks.\n\n"
    )

    report.write("== MITRE ATT&CK Mapping ==\n")
    report.write("T1566 – Phishing\n")
    report.write("TA0001 – Initial Access\n\n")

    report.write("== Recommendation ==\n")
    report.write(
        "- Implement MFA\n"
        "- Add anti-phishing banners\n"
        "- Enforce domain protections (DMARC, SPF, DKIM)\n"
        "- Monitor for lookalike domains\n"
    )

print(f"[+] Report generated: {OUTPUT_FILE}")
