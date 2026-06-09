# SQL Injection Log Analyser

## Overview

SQL Injection Log Analyser is a cybersecurity project developed on Kali Linux that demonstrates how SQL can be used to investigate and detect malicious web application activity. The project simulates web server logs containing both legitimate and malicious requests, stores them in a SQLite database, and uses SQL queries to identify common SQL injection attack patterns.

The project focuses on practical cybersecurity analysis rather than simple database management. By examining web traffic logs, it identifies suspicious requests, malicious IP addresses, failed login attempts, SQLMap activity, and known SQL injection payloads such as `UNION SELECT`, `DROP TABLE`, and `OR 1=1`.

## Features

* Database-driven log storage using SQLite
* Automated import of web server logs using Python
* Detection of common SQL injection techniques
* Identification of suspicious source IP addresses
* Detection of failed authentication attempts
* Analysis of server errors linked to malicious activity
* Automated security reporting and summarisation

## Technologies Used

* Kali Linux
* SQLite
* SQL
* Python
* Git
* GitHub

## Skills Demonstrated

* SQL database design
* Data querying and filtering
* Cybersecurity log analysis
* Threat detection and investigation
* Incident reporting
* Python automation
* Security-focused data analysis

## Key Findings

The analysis successfully identified multiple simulated SQL injection attempts originating from several source IP addresses. Common attack indicators included SQLMap-generated requests, authentication bypass attempts, UNION-based injections, and destructive payloads targeting database structures.

## Learning Outcomes

This project strengthened my understanding of how SQL can be applied in cybersecurity for threat detection, log analysis, and incident investigation. It also provided practical experience working with structured data, developing detection logic, and automating security analysis workflows using Python and SQL.

## Disclaimer

This project uses simulated log data created for educational and portfolio purposes only. No real systems, organisations, or user data were involved.
