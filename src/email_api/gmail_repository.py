from interfaces.email_interface import EmailInterface
from utils.gmail_auth_helper import get_authorized_gmail_service


class GmailRepository(EmailInterface):
    """
    Gmail implementation of EmailInterface
    """
    def __init__(self, gmail_service):
        super().__init__()
        self.gmail_service = gmail_service

    def get_email_ids(self, user_id='me'):
        results = self.gmail_service.users().messages().list(userId=user_id).execute()
        messages = results.get("messages", [])
        return messages

    def get_message(self, message_id):
        """
        Retrieves a specific message.
        """
        try:
            result = self.gmail_service.users().messages().get(userId='me', id=message_id).execute()
            return result
        except HttpError as e:
             logger.error(f"Gmail API failed for ID {message_id}: {e}")
             raise MessageNotFoundError(f"Could not find message {message_id}. Error: {e}") from e

    def get_message_by_id(self, message_id):
        """
        Alias for get_message.
        """
        return self.get_message(message_id)
