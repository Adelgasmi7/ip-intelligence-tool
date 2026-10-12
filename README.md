
# IP Intelligence Tool

A Python-based cybersecurity tool that retrieves and displays intelligence about IP addresses using the ipwho.is API.

This project demonstrates API integration, IP address validation, JSON processing, exception handling, and modular Python programming.

## Features

- Validates IPv4 and IPv6 addresses before performing lookups.
- Retrieves IP geolocation information, including country and city.
- Identifies the Internet Service Provider (ISP) and Autonomous System Number (ASN).
- Generates a formatted IP intelligence report in the terminal.
- Handles invalid IP addresses, HTTP errors, and network request failures.

## Technologies Used

- **Python 3**
- **Requests** — HTTP API requests
- **ipaddress** — IP address validation
- **ipwho.is API** — IP intelligence and geolocation data

## Installation

Clone the repository:

```bash
git clone https://github.com/Adelgasmi7/ip-intelligence-tool.git
cd ip-intelligence-tool
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python main.py
```

Enter an IP address when prompted.

## Example Output

```text
Enter the IP address: 8.8.8.8

======================================
        IP INTELLIGENCE REPORT
======================================
IP Address      8.8.8.8
Country         United States
City            San Jose
ISP             Google LLC
ASN             15169

Lookup Status: SUCCESS
======================================
```

*Geolocation results may vary depending on the API's data.*

## Future Improvements

- Integrate IP reputation and threat intelligence APIs.
- Support bulk IP address lookups.
- Export intelligence reports to JSON or CSV.
- Add automated tests.

## Disclaimer

This project is intended for cybersecurity education, network analysis, and legitimate security investigations.
