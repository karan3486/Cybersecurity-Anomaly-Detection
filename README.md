# Webserver Log Analysis with Flask and OpenAI GPT-4

## Overview
This project is a Flask-based web application that integrates OpenAI GPT-4 to analyze webserver access logs for cybersecurity purposes. It classifies log entries as either "Normal Activity" or "Potential Attack," providing insights into anomalies, suspicious behavior, or malicious patterns.

---

## Features
- **Log Analysis**: Detects whether a log entry indicates normal behavior or a potential attack.
- **OpenAI GPT-4 Integration**: Utilizes GPT-4 for intelligent classification and decision-making.
- **Web Interface**: Provides a simple, user-friendly interface for submitting log entries.
- **REST API**: Exposes an endpoint for programmatic interaction.

---

## Technology Stack
- **Backend**: Flask
- **Frontend**: HTML templates rendered by Flask
- **AI Integration**: OpenAI GPT-4
- **Environment Management**: Python `dotenv` library
- **Dependencies**:
  - `flask`
  - `openai`
  - `dotenv`
  - `os`

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/webserver-log-analysis.git
   cd webserver-log-analysis
