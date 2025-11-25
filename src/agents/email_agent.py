"""
EmailAgent: An agent for various email tasks

Subtasks:
1. Retrieve emails
2. Build prompts
"""



from datetime import datetime
from interfaces import llm_interface

class EmailAgent():

    def __init__(self, llm: llm_interface, max_emails = 50):
        """
        Initialize the EmailAgent with a language model interface and maximum email limit.

        Args:
            llm: a language model for processing email content.
            max_emails (int): Maximum number of emails to process in a single operation.
        """

        self.llm = llm
        self.max_emails = max_emails

    def _build_system_prompt(self) -> str:
        """
        Build the system prompt for email processing tasks.

        Returns:
            str: The system prompt.
        """

        system_prompt = """You are an expert email summarization assistant. Your task is to:
                    1. Identify the key information in each email (sender, subject, main points)
                    2. Categorize emails by priority (High, Medium, Low)
                    3. Extract action items if any
                    4. Provide a concise summary

                    Be clear, factual, and actionable in your summaries."""
        
        return system_prompt
    
    def generate(self, emails: list) -> str:
        """
        Generate a summary of the provided emails using the LLM.

        Args:
            emails (list): A list of email dicts with 'sender', 'subject', and 'body'.

        Returns:
            str: The generated email summary.
        """

        # system_prompt = self._build_system_prompt()
        
        # email_contents = "\n\n".join([f"From: {email['sender']}\nSubject: {email['subject']}\nBody: {email['body']}" for email in emails[:self.max_emails]])
        
        # messages = [
        #     {"role": "system", "content": system_prompt},
        #     {"role": "user", "content": f"Please summarize the following emails:\n\n{email_contents}"}
        # ]
        
        # summary = self.llm.generate(messages, max_tokens=500)

        summary = "This is a placeholder summary of the emails."
        
        return summary







