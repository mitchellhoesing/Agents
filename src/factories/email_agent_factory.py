from agents.email_agent import EmailAgent
from email_api.gmail_repository import GmailRepository
from clients.openai_client import OpenAIClient


class EmailAgentFactory:
    def create_email_agent(provider: str, llm: str) -> EmailAgent:
        if provider == 'gmail':
            email_client = GmailRepository()
        # TODO: Implement other email providers
        # elif provider == 'outlook':
        #     email_client = OutlookRepository()
        # elif provider == 'sendgrid':
        #     email_client = SendGridRepository()
        else:
            raise ValueError(f"Invalid provider: {provider}")

        if llm == 'GPT':
            llm_client = OpenAIClient()
        # TODO: Implement other LLM clients
        # elif llm == 'Claude':
        #     llm_client = AnthropicClient()
        # elif llm == 'Gemini':
        #     llm_client = GeminiClient()
        else:
            raise ValueError(f"Invalid LLM: {llm}")

        return EmailAgent(llm_client, email_client)

