from abc import ABC, abstractmethod

class EmailInterface(ABC):
    """
    Abstract interface for email operations.
    
    Allows for multiple implementations (Gmail, Outlook, SendGrid)
    without changing dependent code. Follows the Dependency Inversion
    Principle - high-level modules depend on this abstraction rather
    than concrete implementations.
    """

    pass

