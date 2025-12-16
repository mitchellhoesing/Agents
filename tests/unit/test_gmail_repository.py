import unittest
from unittest.mock import Mock, MagicMock, patch
from email_api.gmail_repository import GmailRepository

class TestGmailRepositoryUnit(unittest.TestCase):
    def setUp(self):
        self.mock_service = Mock()
        self.repo = GmailRepository(self.mock_service)
    
        self.mock_response_data = {
            'messages': [
                {'id': '16f8d098a58', 'threadId': '16f8d098a58'},
                {'id': '17g9e109b69', 'threadId': '17g9e109b69'}
            ],
            'nextPageToken': 'abc'
        }

        (self.mock_service.users.return_value
             .messages.return_value
             .list.return_value
             .execute.return_value) = self.mock_response_data

    
    def test_get_email_ids_returns_data(self):
        result = self.repo.get_email_ids(user_id='test_user')

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['id'], '16f8d098a58')
        
        self.mock_service.users.assert_called_once()
        self.mock_service.users().messages().list.assert_called_once_with(userId='test_user')