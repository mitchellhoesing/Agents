import unittest
from factories.email_agent_factory import EmailAgentFactory
from agents.email_agent import EmailAgent
from email_api.gmail_repository import GmailRepository
from clients.openai_client import OpenAIClient

class TestEmailAgentFactory(unittest.TestCase):
    def setUp(self):
        self.email_agent = EmailAgentFactory.create_email_agent('gmail', 'GPT')
    
    def test_create_email_agent(self):
        self.assertIsInstance(self.email_agent, EmailAgent)
        self.assertIsInstance(self.email_agent.email_client, GmailRepository)
        self.assertIsInstance(self.email_agent.llm, OpenAIClient)

    def test_create_email_agent_invalid_provider(self):
        self.assertRaises(ValueError, EmailAgentFactory.create_email_agent, 'invalid', 'GPT')

    def test_create_email_agent_invalid_llm(self):
        self.assertRaises(ValueError, EmailAgentFactory.create_email_agent, 'gmail', 'invalid')
        
