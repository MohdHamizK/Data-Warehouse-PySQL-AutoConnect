# Sales Data Warehouse Automation

A modular Python-based system for refreshing materialized views, querying sales data, and sending automated reports via email.

## Features
- PostgreSQL star schema
- Email notifications with HTML and CSV attachments
- Logging and error handling
- CLI commands for automation

## Setup
1. `pip install -r requirements.txt`
2. Create `.env` from `.env.example`
3. Run: `send-sales-report refresh-mv` or `send-sales-report send-report`

## Tech Stack
- Python
- PostgreSQL
- Gmail SMTP
- Draw.io ERD