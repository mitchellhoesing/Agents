"""
Interface module for Large Language Models (LLMs).
"""

from abc import ABC, abstractmethod

class LLMClient(ABC):
    """
    Abstract base class for Large Language Model clients.
    """

    @abstractmethod
    def generate(self, messages:list, max_tokens:int=150) -> str:
        """
        Generate a response from the LLM based on the provided messages.

        Args:
            messages (list): A list of message dicts with 'role' and 'content'.
            max_tokens (int): Maximum number of tokens to generate.

        returns:
            str: The generated response from the LLM.
        """

        pass

    

    


