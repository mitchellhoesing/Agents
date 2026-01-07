import json

from utils.text_processor import TextProcessor
from dataclasses import dataclass


@dataclass
class EmailData:
    subject: str
    body: str
    sender: str
    date: str
    id: str

class GmailParser:
    def __init__(self):
        self.text_processor = TextProcessor()

    def parse_email(self, message) -> EmailData:
        return EmailData(
            id=message_id,
            subject=self._extract_subject(raw_message),
            sender=self._extract_sender(raw_message),
            body=self._extract_body(raw_message),
            labels=self._extract_labels(raw_message)
        )

    def _extract_message_with_parts(self, message) -> list:
        parts = []
        for part in message['payload']['parts']:
            if part['mimeType'] in ('text/plain', 'text/html') and 'data' in part['body']:
            
                data = part['body']['data']
                text = self.text_processor.decode_message(data)
                
                if part['mimeType'] == 'text/html':
                    text = self.text_processor.strip_html(text)
                parts.append(text)
        
        combined_text = '\n\n'.join(parts)

        return combined_text


    def _extract_simple_message(self, message) -> str:
        data = message['payload']['body']['data']
        text = self.text_processor.decode_message(data)

        if message['payload']['mimeType'] == 'text/html':
            text = self.text_processor.strip_html(text)
            
        return text

    def _extract_messages_text(self, batch_results) -> list:
        decoded_messages = []
        for message in batch_results:
            text = None
            if 'parts' in message['payload']:
                text = self._extract_message_with_parts(message)
            else:
                text = self._extract_simple_message(message)
            
            text = self.text_processor.clean_whitespace(text)
            print(text)
            if text:
                decoded_messages.append({
                    'id': message['id'],
                    'text': text
                })

        return decoded_messages

if __name__ == '__main__':
    parser = GmailParser()
    batch_results = json.load(open(r'..\..\..\json_batch_data\batch_results.json'))
    parser._extract_messages_text(batch_results)