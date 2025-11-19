from interfaces.LLMInterface import LLMInterface
from abc import abstractmethod

class BaseLLMClient(LLMInterface):
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

    def _combine_prompts(self, system_prompt:str, user_query:str) -> str:
        """
        Combine system and user prompts into a single prompt.

        Args:
            system_prompt (str): The system prompt.
            user_query (str): The user prompt.
        Returns:
            None
        """

        system_prompt = """You are an expert email summarization assistant. Your task is to:
                    1. Identify the key information in each email (sender, subject, main points)
                    2. Categorize emails by priority (High, Medium, Low)
                    3. Extract action items if any
                    4. Provide a concise summary

                    Be clear, factual, and actionable in your summaries."""
        
        combined_prompt = f"{system_prompt}\n\nUser Query: {user_query}"
        
        return combined_prompt

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
        agent_query = self._combine_prompts

        return user_query