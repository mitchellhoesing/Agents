import unittest
import sys
import os

from unittest.mock import patch

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from clients.openai_client import OpenAIClient

class TestBaseLLMClient(unittest.TestCase):

    def setUp(self):
        self.llm_client = OpenAIClient()

    def test_read_user_query(self):
        # Mock the built-in input function
        with patch('builtins.input', return_value='What is the capital of France?'):
            user_query = self.llm_client.read_user_query()
            self.assertEqual(user_query, 'What is the capital of France?')


if __name__ == '__main__':
    unittest.main()