import unittest

from unittest.mock import patch, Mock, MagicMock
from email_api.gmail_repository import GmailRepository
from utils.gmail_auth_helper import get_authorized_gmail_service

class TestGmailRepository(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test."""
        gmail_service = get_authorized_gmail_service()
        self.client = GmailRepository(gmail_service)

    def test_get_email_ids(self):
        """Test the list_inbox_messages method."""
        self.assertIsInstance(self.client.get_email_ids(), list)

if __name__ == '__main__':
    unittest.main()