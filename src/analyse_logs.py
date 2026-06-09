import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "security_logs.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

detection_filter = """
url LIKE '%UNION SELECT%'
OR url LIKE '%DROP TABLE%'
OR url LIKE '% OR 1=1%'
OR url LIKE '%--%'
OR url LIKE "%' OR %"
OR user_agent LIKE '%sqlmap%'
"""

cursor.execute("SELECT COUNT(*) FROM web_logs")
total_logs = cursor.fetchone()[0]

cursor.execute(f"SELECT COUNT(*) FROM web_logs WHERE {detection_filter}")
suspicious_logs = cursor.fetchone()[0]

cursor.execute(f"""
SELECT ip_address, COUNT(*) AS count
FROM web_logs
WHERE {detection_filter}
GROUP BY ip_address
ORDER BY count DESC
LIMIT 1
""")
top_ip = cursor.fetchone()

print("\n===== SECURITY REPORT =====\n")
print(f"Total Logs Analysed: {total_logs}")
print(f"Suspicious Requests Found: {suspicious_logs}")

if top_ip:
	print(f"Top Suspicious IP: {top_ip[0]}")
	print(f"Requests From This IP: {top_ip[1]}")

print("\n================================\n")

conn.close()
