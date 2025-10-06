
from datetime import datetime

class EmailAgent:

    def __init__(self, llm_interface, max_emails = 50):
        """
        Initialize the EmailAgent with a language model interface and maximum email limit.

        Args:
            llm_interface: An instance of a language model interface for processing email content.
            max_emails (int): Maximum number of emails to process in a single operation.
        """

        self.llm = llm_interface
        self.max_emails = max_emails
        self.system_prompt = self._build_system_prompt()

    def _build_system_prompt(self):
        """
        Build the system prompt for the language model for email summarization.

        Returns:
            str: The constructed system prompt.
        """
        prompt = """You are an expert email summarization assistant. Your task is to:
                    1. Identify the key information in each email (sender, subject, main points)
                    2. Categorize emails by priority (High, Medium, Low)
                    3. Extract action items if any
                    4. Provide a concise summary

                    Be clear, factual, and actionable in your summaries."""

        return prompt

    def summarize_single_email(self, email: dict) -> dict:
        """
        Summarize a single email
        
        Args:
            email: dict with keys 'from', 'subject', 'body', 'date'
            
        Returns:
            dict with summary, priority, and action items
        """
        prompt = f"""Summarize this email:

        From: {email.get('from', 'Unknown')}
        Subject: {email.get('subject', 'No subject')}
        Date: {email.get('date', 'Unknown')}

        Body:
        {email.get('body', '')}

        Provide:
        1. A 2-3 sentence summary
        2. Priority level (High/Medium/Low)
        3. Action items (if any)"""

        response = self.llm.generate(
            system_prompt=self.system_prompt,
            user_prompt=prompt
        )
        
        return {
            'original': email,
            'summary': response,
            'timestamp': datetime.now().isoformat()
        }



