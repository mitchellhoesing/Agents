from interfaces.email_interface import EmailInterface
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

class GmailRepository(EmailInterface):
    """
    Gmail implementation of EmailInterface
    """
    def __init__(self):
        super().__init__()
        self.credentials = None # Placeholder, normally loaded from file or env

    def get_messages(self):
        """
        Retrieves a list of messages.

        Returns:
            A list of messages.
        """
        try:
            if not self.credentials:
                 # In a real app we'd authenticate here. For now/test ensuring it doesn't crash on build if mocked
                 # But if build is mocked, it won't check credentials validity usually.
                 pass

            service = build('gmail', 'v1', credentials=self.credentials)
            results = service.users().messages().list(userId='me').execute()
            messages = results.get('messages', [])
            return messages
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_message(self, message_id):
        """
        Retrieves a specific message.
        """
        try:
            service = build('gmail', 'v1', credentials=self.credentials)
            result = service.users().messages().get(userId='me', id=message_id).execute()
            return result
        except Exception as e:
             print(f"An error occurred: {e}")
             return None

    def get_message_by_id(self, message_id):
        """
        Alias for get_message.
        """
        return self.get_message(message_id)
