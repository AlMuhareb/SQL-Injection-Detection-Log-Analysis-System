

CREATE TABLE IF NOT EXISTS web_logs (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	timestamp TEXT NOT NULL,
	ip_address TEXT NOT NULL,
	http_method TEXT NOT NULL,
	url TEXT NOT NULL,
	status_code INTEGER NOT NULL,
	user_agent TEXT
);
