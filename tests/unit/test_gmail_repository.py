import unittest

from unittest.mock import patch, Mock, MagicMock
from email_api.gmail_repository import GmailRepository


class TestGmailRepository(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test."""
        self.client = GmailRepository()

    def test_get_messages(self):
        """Test the get_messages method."""
        with patch('email_api.gmail_repository.build') as mock_build:
            mock_build.return_value.users().messages().list().execute.return_value = {'messages': []}
            self.assertEqual(self.client.get_messages(), [])

    def test_get_message(self):
        """Test the get_message method."""
        with patch('email_api.gmail_repository.build') as mock_build:
            mock_build.return_value.users().messages().get().execute.return_value = {'id': '1'}
            self.assertEqual(self.client.get_message('1'), {'id': '1'})

    def test_get_message_by_id(self):
        """Test the get_message_by_id method."""
        with patch('email_api.gmail_repository.build') as mock_build:
            mock_build.return_value.users().messages().get().execute.return_value = {'id': '1'}
            self.assertEqual(self.client.get_message_by_id('1'), {'id': '1'})





if __name__ == '__main__':
    unittest.main()