import unittest

from agents.email_agent import EmailAgent  # Adjusted import path


class TestEmailAgent(unittest.TestCase):

    def setUp(self):
        self.email_agent = EmailAgent(llm=None, email_client=None)

    def test_build_system_prompt(self):
        self.expected_prompt = """You are an expert email summarization assistant. Your task is to:
                    1. Identify the key information in each email (sender, subject, main points)
                    2. Categorize emails by priority (High, Medium, Low)
                    3. Extract action items if any
                    4. Provide a concise summary

                    Be clear, factual, and actionable in your summaries."""
        
        self.assertEqual(self.email_agent._build_system_prompt(), self.expected_prompt)

if __name__ == '__main__':
    unittest.main()

