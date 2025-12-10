import unittest

from unittest.mock import patch
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