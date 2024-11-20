# ZIP Code Validator

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Requests Library](https://img.shields.io/badge/requests-%5E2.0-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen)


## Description

The **ZIP Code Validator** is a Python script that validates ZIP codes using the USPS City/State Lookup API. It takes an input CSV file containing ZIP codes, retrieves the corresponding city, state, and county information, and writes the results to an output CSV file.

---

## Features

- Validates ZIP codes using the USPS API.
- Provides city, state, and placeholder county information.
- Handles errors gracefully, marking invalid or failed lookups.
- Processes input CSV files and outputs results in a structured format.

---

## Prerequisites

- Python 3.7 or higher
- Modules: `requests`, `csv`, `xml.etree.ElementTree`
- USPS User ID (register for free at [USPS Registration](https://reg.usps.com/entreg/RegistrationAction_input))

---

## Installation

1. Clone or download the repository.
2. Install the required Python packages:
   ```bash
   pip install requests
   ```

---

## Usage
1. Register for a USPS User ID if you don’t have one. Visit [USPS Registration](https://reg.usps.com/entreg/RegistrationAction_input) to sign up.
2. Replace the placeholder `USPS_USER_ID` in the script with your USPS User ID.
3. Prepare an input CSV file named `zipcodes.csv` with ZIP codes in the first column. Example:

   ```
   ZIP Code
   10001
   90210
   ```

2. Run the script:
   ```bash
   python zip_code_validator.py
   ```

3. The output will be saved in a file named `validated_zipcodes.csv` with the following format:
   ```
   ZIP Code,City,State,County
   10001,New York,NY,Unavailable
   90210,Beverly Hills,CA,Unavailable
   ```

---

## Configuration

- Update the variable `USPS_USER_ID` in the script with your USPS User ID.

---

## Notes

- The script marks the county as "Unavailable" because the USPS API does not provide this information. You may extend the script to fetch county data from other APIs if needed.

---

## License

This project is open-source and licensed under the MIT License.

---

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/zip-code-validator/issues).

---

## Disclaimer

This script is intended for educational purposes. Ensure compliance with USPS API usage terms and conditions.