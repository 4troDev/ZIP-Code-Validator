import csv  # Module for working with CSV files
import requests  # Module for sending HTTP requests
import xml.etree.ElementTree as ET  # Module for parsing XML data

# USPS API configuration
USPS_USER_ID = 'USPS_User'  # Replace with your USPS User ID

def validate_zipcode(zipcode):
    """
    Validate a single ZIP code using the USPS API and return city, state, and county information.
    
    Parameters:
        zipcode (str): The ZIP code to validate.

    Returns:
        tuple: A tuple containing ZIP code, city, state, and county (if available).
    """
    # USPS API URL for City/State lookup
    url = f"http://production.shippingapis.com/ShippingAPI.dll?API=CityStateLookup&XML=<CityStateLookupRequest USERID='{USPS_USER_ID}'><ZipCode ID='0'><Zip5>{zipcode}</Zip5></ZipCode></CityStateLookupRequest>"
    
    # Send HTTP GET request to USPS API
    response = requests.get(url)

    if response.status_code == 200:  # Check if the request was successful
        # Parse the XML response
        root = ET.fromstring(response.content)
        
        try:
            # Extract city and state from the XML
            city = root.find(".//City").text
            state = root.find(".//State").text
            county = "Unavailable"  # Placeholder, as USPS API doesn't provide county info
            return zipcode, city, state, county
        except AttributeError:  # Handle invalid ZIP codes
            return zipcode, "Invalid ZIP Code", "", ""
    else:
        # Handle errors in API request
        print(f"Failed to fetch data for ZIP code {zipcode}. Status code: {response.status_code}")
        return zipcode, "Error", "", ""

def validate_zipcodes_from_csv(input_csv, output_csv):
    """
    Validate ZIP codes from an input CSV file and save the results to an output CSV.
    
    Parameters:
        input_csv (str): Path to the input CSV file containing ZIP codes.
        output_csv (str): Path to the output CSV file where results will be saved.
    """
    with open(input_csv, mode='r') as infile, open(output_csv, mode='w', newline='') as outfile:
        reader = csv.reader(infile)  # Read rows from the input CSV
        writer = csv.writer(outfile)  # Write rows to the output CSV
        writer.writerow(["ZIP Code", "City", "State", "County"])  # Write header row to the output CSV
        
        next(reader, None)  # Skip the header row in the input CSV
        for row in reader:
            zipcode = row[0]  # Assume ZIP code is in the first column
            validated_data = validate_zipcode(zipcode)  # Validate the ZIP code
            writer.writerow(validated_data)  # Write the results to the output CSV

# Specify input and output CSV file paths
input_csv_file = 'zipcodes.csv'  # Input CSV file with ZIP codes (single column or first column is ZIP codes)
output_csv_file = 'validated_zipcodes.csv'  # Output CSV file

# Run the validation process
validate_zipcodes_from_csv(input_csv_file, output_csv_file)
print("Validation complete. Check validated_zipcodes.csv for results.")
