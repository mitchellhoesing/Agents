"""
Interface module for Large Language Models (LLMs).

generate_reponse(): 
read_user_prompt()
combine_prompts()
evaluate_response()
log_trace()
"""

from abc import ABC, abstractmethod

class LLMClient(ABC):
    """
    Abstract base class for Large Language Model clients.
    """

    @abstractmethod
    def generate_response(self, messages:list, max_tokens:int=150) -> str:
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
    def read_user_prompt(self, prompt_file:str) -> None:
        """
        Read a user prompt from a file.

        Args:
            prompt_file (str): Path to the prompt file.
        Returns:
            None
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
    
    

    


