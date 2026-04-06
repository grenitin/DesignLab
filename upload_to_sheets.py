import os
import csv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json

# Configuration
CSV_FILE_PATH = "usability_evaluation.csv"
CREDENTIALS_FILE = "credentials.json"

# You will need to put your Google Sheet ID here!
# For example, if your URL is https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
# The SPREADSHEET_ID is "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
SPREADSHEET_ID = "YOUR_SPREADSHEET_ID_HERE"
RANGE_NAME = "Sheet1!A1" # Target sheet name and starting cell

def get_google_sheets_service():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
    service = build("sheets", "v4", credentials=creds)
    return service

def upload_csv_to_sheets():
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"Error: Could not find {CREDENTIALS_FILE}.")
        print("Please securely save your Google Service Account JSON key in this folder.")
        return

    if SPREADSHEET_ID == "YOUR_SPREADSHEET_ID_HERE":
        print("Error: Please replace 'YOUR_SPREADSHEET_ID_HERE' with your actual Google Sheet ID in the script.")
        return

    print("Connecting to Google Sheets...")
    service = get_google_sheets_service()
    sheet = service.spreadsheets()

    # Read the CSV data
    print(f"Reading data from {CSV_FILE_PATH}...")
    with open(CSV_FILE_PATH, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Prepare the API payload
    body = {
        "values": data
    }

    print("Uploading data to Google Sheets...")
    try:
        # We use valueInputOption="USER_ENTERED" so sheets formats numbers and text properly
        result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption="USER_ENTERED",
            body=body
        ).execute()

        print(f"✅ Success! {result.get('updatedCells')} cells updated in your Google Sheet.")
    except Exception as e:
        print(f"❌ Failed to upload data: {e}")

if __name__ == "__main__":
    upload_csv_to_sheets()
