import base64
import re

from bs4 import BeautifulSoup

class TextProcessor:
    def __init__(self):
        pass
    
    def strip_html(self, html) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        return text
        
    @staticmethod
    def clean_whitespace(text: str) -> str:
        """Remove excessive whitespace and special characters."""
        # Remove soft hyphens and other invisible characters
        text = text.replace('\xad', '')
        text = text.replace('\u2007', '')  # Figure space
        text = text.replace('\xa0', ' ')   # Non-breaking space
        text = text.replace('\r\n', '\n')  # Normalize line breaks

        # Matches URLs with protocol
        text = re.sub(r'https?://[^\s<>"{}|\\^`\[\]]+', '', text)
        text = re.sub(r'ftp://[^\s<>"{}|\\^`\[\]]+', '', text)
        
        # Matches www. URLs without protocol
        text = re.sub(r'www\.[^\s<>"{}|\\^`\[\]]+', '', text)

        # Matches query parameters
        text = re.sub(r'\?[\w\d&=\-_%.]+', '', text)
        
        # Sub special characters with space. Exclude common punctuation
        text = re.sub(r'[^a-zA-Z0-9\s.,?;:\'"]', ' ', text)
        
        # Replace multiple whitespace with single space
        text = re.sub(r'\s+', ' ', text)
        
        # Remove multiple newlines
        text = re.sub(r'\n\s*\n', '\n\n', text)


        
        return text.strip()

    def decode_message(self, message) -> str:
        text = base64.urlsafe_b64decode(message).decode('utf-8')
        return text