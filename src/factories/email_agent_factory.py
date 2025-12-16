from agents.email_agent import EmailAgent
from email_api.gmail_repository import GmailRepository
from clients.openai_client import OpenAIClient
from utils.gmail_auth_helper import get_authorized_gmail_service

class EmailAgentFactory:
    def create_email_agent(email_service: str, llm: str) -> EmailAgent:
        if email_service.lower() == 'gmail':
            gmail_service = get_authorized_gmail_service()
            if not gmail_service:
                raise RuntimeError("Failed to authenticate with Gmail")
            email_client = GmailRepository(gmail_service)
        # TODO: Implement other email providers
        # elif email_service.lower() == 'outlook':
        #     email_client = OutlookRepository()
        # elif email_service.lower() == 'sendgrid':
        #     email_client = SendGridRepository()
        else:
            raise ValueError(f"Invalid email_service: \"{email_service}\"")

        if llm.lower() == 'gpt':
            llm_client = OpenAIClient()
        # TODO: Implement other LLM clients
        # elif llm.lower() == 'claude':
        #     llm_client = AnthropicClient()
        # elif llm.lower() == 'gemini':
        #     llm_client = GeminiClient()
        else:
            raise ValueError(f"Invalid LLM: \"{llm}\"")

        return EmailAgent(llm_client, email_client)

