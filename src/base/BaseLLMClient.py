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
    def combine_prompts(self, system_prompt:str, user_prompt:str) -> None:
        """
        Combine system and user prompts into a single prompt.

        Args:
            system_prompt (str): The system prompt.
            user_prompt (str): The user prompt.
        Returns:
            None
        """
        pass

    @abstractmethod
    def generate_log_trace(self, interaction_details:dict) -> dict:
        """
        Generate a log trace of the LLM interaction.

        Args:
            interaction_details (dict): Details of the interaction to log.
        Returns:
            dict: The trace of the LLM Client pipeline.
        """
        pass

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