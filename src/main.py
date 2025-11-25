from agents.email_agent import EmailAgent
"""

Process:
User chooses which LLM to use. -> Implement an LLM interface.
User prompts the agent with an email-related task. -> Add to the system prompt
Agent is provided with tools to perform email tasks. -> Write tool interfaces, parse agent output for tool call
Tool calls are made as needed to complete the task. -> add tool output to agent context
The agent composes a final response to the user with all given information. -> Have the LLM review and revise its output.

Class: EmailAgent
User chooses which LLM to use. -> Implement an LLM interface. 
User prompts the agent with an email-related task. -> Add to the system prompt Class: Email Agent
Tool calls are made as needed to complete the task. -> add tool output to agent context. Class: Email Agent
The agent composes a final response to the user with all given information. -> Have the LLM review and revise its output.
Evaluate outputs
Define mocks for external calls.

Class: Tool Interface
Agent is provided with tools to perform email tasks. -> Write tool interfaces, parse agent output for tool call.
Define mocks for external calls.

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

def main():
    email_agent = EmailAgent(llm=None)

if __name__ == "__main__":
    main()
