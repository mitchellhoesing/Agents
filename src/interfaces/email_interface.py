from abc import ABC, abstractmethod

class EmailInterface(ABC):

    @abstractmethod
    def get_messages():
        """
        Retrieves a list of messages.

        Returns:
            A list of messages.
        """
        pass

