import openai

from base import BaseLLMClient


class OpenAIClient(BaseLLMClient):
    """
    Open AI implementation of LLMInterface
    """
    def __init__(self, default_model: str = "gpt-3.5-turbo"):
        self.default_model = default_model

    def generate(self, messages: list, max_tokens: int = 150) -> str:
        """
        Generate a response from the OpenAI LLM based on the provided messages.

        Args:
            messages (list): A list of message dicts with 'role' and 'content'.
            max_tokens (int): Maximum number of tokens to generate.
        """

        response = openai.ChatCompletion.create(
            model=self.default_model,
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message['content']