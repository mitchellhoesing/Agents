import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def get_authorized_gmail_service():
    creds = None
    TOKEN_PATH = '../../config/token.json'
    CREDENTIALS_PATH = '../../config/credentials.json'

    # --- STEP 1: Attempt to load existing token ---
    if os.path.exists(TOKEN_PATH):
        try:
            # Load the credentials from the token file
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
        except Exception as e:
            # Handle case where file exists but is corrupted/unreadable
            print(f"Error loading existing token file: {e}. Re-running full flow.")
            creds = None # Force full re-authorization

    # --- CORE LOGIC: Get VALID credentials (runs if creds is None OR expired) ---
    if not creds or not creds.valid:
    
    # 2a. Attempt non-interactive refresh if possible
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Token expired. Attempting non-interactive refresh...")
                creds.refresh(Request())
            except Exception as e:
                # Refresh failed (e.g., token revoked/invalid_grant)
                print(f"Refresh failed: {e}. Falling back to full authorization flow.")
                creds = None # Force full re-authorization
    
    # 2b. Start full interactive authorization flow
        if not creds:
            print("Starting full interactive authorization flow...")
            try:
                # This uses 'credentials.json' to open a browser window for user consent.
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            except FileNotFoundError:
                print(f"FATAL ERROR: Credentials file not found at {CREDENTIALS_PATH}")
                return None
            except Exception as e:
                print(f"Authorization flow failed: {e}")
                return None

        # --- Save the new/refreshed token for the next run ---
        if creds: # Ensure we have valid credentials before saving
            with open(TOKEN_PATH, 'w') as token:
                token.write(creds.to_json())
            print("New token saved successfully.")

    # --- STEP 3: Build the Service ---
    service = None
    if creds:
        try:
            # The single 'creds' object is passed to the build function.
            service = build('gmail', 'v1', credentials=creds)
            print("Gmail API Service built successfully!")
        except Exception as e:
            print(f"Error building service: {e}")

    return service