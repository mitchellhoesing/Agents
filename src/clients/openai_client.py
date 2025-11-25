import openai

from base.BaseLLMClient import BaseLLMClient


class OpenAIClient(BaseLLMClient):
    """
    Open AI implementation of LLMInterface
    """
    def __init__(self, default_model: str = "gpt-3.5-turbo"):
        super().__init__()
        self.default_model = default_model

    def generate_response(self, messages: list, user_query: str, max_tokens: int = 150) -> str:
        """
        Generate a response from the OpenAI LLM based on the provided messages.

        Args:
            messages (list): A list of message dicts with 'role' and 'content'.
            max_tokens (int): Maximum number of tokens to generate.
        """
    
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_query}
        ]
        response = openai.ChatCompletion.create(
            model=self.default_model,
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message['content']

    # TODO: Implement logging functionality
    def generate_log_trace(self, interaction_details:dict) -> dict:
        """
        Generate a log trace of the LLM interaction.

        Args:
            interaction_details (dict): Details of the interaction to log.
        Returns:
            dict: The trace of the LLM Client pipeline.
        """
        pass