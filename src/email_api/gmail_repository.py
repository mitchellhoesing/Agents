import base64
import json

from interfaces.email_interface import EmailInterface
from utils.gmail_auth_helper import get_authorized_gmail_service
from dataclasses import dataclass

@dataclass
class EmailData:
    subject: str
    body: str
    sender: str
    date: str
    id: str


class GmailRepository(EmailInterface):
    """
    Gmail implementation of EmailInterface
    """
    def __init__(self, gmail_service):
        super().__init__()
        self.batch_results = []
        self.gmail_service = gmail_service

    def message_callback(self,request_id, response, exception) -> None:
        if exception is not None:
            print(f'The API returned an error: {exception}')
        else:
            self.batch_results.append(response)


    def get_email_batch(self) -> None:
        emails = {}
        batch = self.gmail_service.new_batch_http_request(callback=self.message_callback)

        message_ids = self._get_message_ids()
        for message_id in message_ids:
            batch.add(self.gmail_service.users().messages().get(userId='me', id=message_id['id']), request_id=message_id['id'])

        batch.execute()

    def extract_email_data(self, message) -> EmailData:

        return EmailData(
            id=message_id,
            subject=self._extract_subject(raw_message),
            sender=self._extract_sender(raw_message),
            body=self._extract_body(raw_message),
            labels=self._extract_labels(raw_message)
        )


    def _get_message_ids(self, user_id='me') -> list:
        results = self.gmail_service.users().messages().list(
            userId=user_id,
            maxResults=20,
            labelIds=['INBOX']
            ).execute()
        message_ids = results.get("messages", [])

        return message_ids

    def _get_messages_by_id(self) -> list:
        messages = []
        message_ids = self._get_message_ids()
        for message_id in message_ids:
            msg = self.gmail_service.users().messages().get(userId='me', id=message_id['id']).execute()
            messages.append(msg)

        return messages

    def _extract_message_text(self) -> str:
        messages = self._get_messages_by_id()
        for message in messages:
            if 'parts' in message['payload']:
                for part in message['payload']['parts']:
                    if part['mimeType'] in ('text/plain', 'text/html'):
                        data = part['body']['data']
                        return base64.urlsafe_b64decode(data).decode('utf-8')
            else:
                # Simple message with no parts
                data = message['payload']['body']['data']
                return base64.urlsafe_b64decode(data).decode('utf-8')

if __name__ == "__main__":
    gmail_service = get_authorized_gmail_service()
    repo = GmailRepository(gmail_service)
    repo.get_email_batch()