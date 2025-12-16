import unittest
from factories.email_agent_factory import EmailAgentFactory
from agents.email_agent import EmailAgent
from email_api.gmail_repository import GmailRepository
from clients.openai_client import OpenAIClient
from unittest.mock import patch, MagicMock

class TestEmailAgentFactory(unittest.TestCase):

    @patch('factories.email_agent_factory.get_authorized_gmail_service')
    def test_create_email_agent(self, mock_get_authorized_gmail_service):
        mock_service_mock = MagicMock(name='MockGmailService')
        mock_get_authorized_gmail_service.return_value = mock_service_mock
        self.email_agent = EmailAgentFactory.create_email_agent('gmail', 'GPT')

        mock_get_authorized_gmail_service.assert_called_once()
        self.assertIs(self.email_agent.email_client.gmail_service, mock_service_mock)

        self.assertIsInstance(self.email_agent, EmailAgent)
        self.assertIsInstance(self.email_agent.email_client, GmailRepository)
        self.assertIsInstance(self.email_agent.llm, OpenAIClient) 

    @patch('factories.email_agent_factory.get_authorized_gmail_service')
    def test_create_email_agent_if_failed_connection(self, mock_get_authorized_gmail_service):
        mock_get_authorized_gmail_service.return_value = None

        with self.assertRaisesRegex(RuntimeError, 'Failed to authenticate with Gmail'):
            EmailAgentFactory.create_email_agent(email_service='gmail', llm='GPT')

        mock_get_authorized_gmail_service.assert_called_once()

    def test_create_email_agent_invalid_email_service(self):
        with self.assertRaisesRegex(ValueError, "Invalid email_service: \"invalid\""):
            EmailAgentFactory.create_email_agent(email_service='invalid', llm='GPT')

    @patch('factories.email_agent_factory.get_authorized_gmail_service')
    def test_create_email_agent_invalid_llm(self, mock_get_authorized_gmail_service):
        mock_service_mock = MagicMock(name='MockGmailService')
        mock_get_authorized_gmail_service.return_value = mock_service_mock

        with self.assertRaisesRegex(ValueError, "Invalid LLM: \"invalid\""):
            EmailAgentFactory.create_email_agent(email_service='gmail', llm='invalid')

        mock_get_authorized_gmail_service.assert_called_once()
        
