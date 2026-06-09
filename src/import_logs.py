import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "security_logs.db"
CSV_PATH = BASE_DIR / "data" / "web_logs.csv"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open(CSV_PATH, newline="") as csvfile:
	reader = csv.DictReader(csvfile)

	
	count = 0
	for row in reader:
		cursor.execute(
			"""
			INSERT INTO web_logs (
				timestamp,
				ip_address,
				http_method,
				url,
				status_code,
				user_agent
			)
			VALUES (?, ?, ?, ?, ?, ?)
			""",
			(
				row["timestamp"],
				row["ip_address"],
				row["http_method"],
				row["url"],
				int(row["status_code"]),
				row["user_agent"],
			),
		)
		count += 1

conn.commit()
conn.close()

print(f"Imported {count} web log records into the database.")
