"""
EmailAgent: An agent for various email tasks

Subtasks:
1. Retrieve emails
2. Build prompts


Process:
User chooses which LLM to use. -> Implement an LLM interface.
User prompts the agent with an email-related task. -> Add to the system prompt
Agent is provided with tools to perform email tasks. -> Write tool interfaces, parse agent output for tool call
Tool calls are made as needed to complete the task. -> add tool output to agent context
The agent composes a final response to the user with all given information. -> Have the LLM review and revise its output.


Evals:
Evaluate each step in the trace.
Objective:
1. Which tool calls were made?
2. Were the tool calls appropriate for the task?
3. Was the task completed correctly?
4. Were all tasks performed?
5. Time taken to complete the task?
6. Check any factual data vs ground truth

Subjective:
1. Is the tone appropriate
2. Is the summary accurate?
3. Is the summary complete?

"""



from datetime import datetime

class EmailAgent:

    def __init__(self, llm, max_emails = 50):
        """
        Initialize the EmailAgent with a language model interface and maximum email limit.

        Args:
            llm: a language model for processing email content.
            max_emails (int): Maximum number of emails to process in a single operation.
        """

        self.llm = llm
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



