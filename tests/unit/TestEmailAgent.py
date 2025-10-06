import unittest

from src.agents.EmailAgent import EmailAgent


class TestEmailAgent(unittest.TestCase):

    def __init__(self):
        self.email_agent = EmailAgent(llm_interface=None)

    def test_build_system_prompt(self):
        self.expected_prompt = """You are an expert email summarization assistant. Your task is to:
                    1. Identify the key information in each email (sender, subject, main points)
                    2. Categorize emails by priority (High, Medium, Low)
                    3. Extract action items if any
                    4. Provide a concise summary

                    Be clear, factual, and actionable in your summaries."""
        
        self.assertequal(self.email_agent._build_system_prompt(), self.expected_prompt)
    
if __name__ == '__main__':
    unittest.main()
