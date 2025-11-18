import unittest
import sys
import os

# Add the src directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

from base.BaseLLMClient import BaseLLMClient

class TestBaseLLMClient(unittest.TestCase):

    def setUp(self):
        self.llm_client = BaseLLMClient()

    def test_read_user_query(self):
        # Since read_user_query uses input(), we will mock it for testing
        input_values = ['What is the capital of France?']
        def mock_input(s):
            return input_values.pop(0)
        
        self.llm_client.input = mock_input
        
        user_query = self.llm_client.read_user_query()
        self.assertEqual(user_query, 'What is the capital of France?')