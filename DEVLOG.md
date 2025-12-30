### NEXT:
- Implement Google Gmail API and retrieve emails

### TODO:
- Implement OpenAI Client
- Implement agent trace evaluations
- Implement tool interface
- Separate the email agent factory into an LLM service factory and an email service factory. The email agent factory will simply be an orchestrator.
- Implement tool call parsing
- Implement tool call execution
- Implement tool call logging
- Implement factory for agent creation
- Ensure email interface includes all methods to be enforced
- Ensure method type hints exist for all methods
- Ensure all methods have docstrings

### 2025-12-16
- Fixed Factory tests. Do not want to create a gmail api connection for unittests

### 2025-12-07
- Fixed sys.path import hack. Added pyproject.toml. Generated new requirements.txt



