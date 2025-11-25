import unittest
import os
import sys
from unittest.mock import patch, Mock, MagicMock

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from clients.openai_client import OpenAIClient


class TestOpenAIClient(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test."""
        self.client = OpenAIClient()
    
    @patch('openai.ChatCompletion.create')
    def test_generate_response_success(self, mock_create):
        """Test successful response generation."""
        # Arrange
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message = {'content': 'Paris is the capital of France.'}
        mock_create.return_value = mock_response
        
        user_query = "What is the capital of France?"
        
        # Act
        result = self.client.generate_response([], user_query)
        
        # Assert
        self.assertEqual(result, 'Paris is the capital of France.')
        mock_create.assert_called_once()


if __name__ == '__main__':
    unittest.main()