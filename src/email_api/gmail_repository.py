from interfaces.email_interface import EmailInterface
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

class GmailRepository(EmailInterface):
    """
    Gmail implementation of EmailInterface
    """
    def __init__(self):
        super().__init__()

    def get_messages(self):
        """
        Retrieves a list of messages.

        Returns:
            A list of messages.
        """
        try:
            service = build('gmail', 'v1', credentials=self.credentials)
            results = service.users().messages().list(userId='me').execute()
            messages = results.get('messages', [])
            return messages
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
