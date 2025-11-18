from interfaces.LLMInterface import LLMClient
from abc import abstractmethod

class BaseLLMClient(LLMClient):
    """
    Base implementation of LLMInterface
    """

    @abstractmethod
    def generate_response(self, messages: list, max_tokens: int = 150) -> str:
        """
        Generate a response from the LLM based on the provided messages.

        Args:
            messages (list): A list of message dicts with 'role' and 'content'.
            max_tokens (int): Maximum number of tokens to generate.

        Returns:
            str: The generated response from the LLM.
        """
        pass

    @abstractmethod
    def read_user_query(self) -> str:
        """
        Read user query stdin.

        Args:
            None
        Returns:
            the user prompt as a string.
        """
        user_query = input("Please enter your query: ")

        return user_query