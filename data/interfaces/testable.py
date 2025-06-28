from abc import ABC, abstractmethod

class Testable(ABC):
    """
    Interface for any class that supports test execution.
    """

    @abstractmethod
    def run_tests(self) -> None:
        """
        Executes a series of tests.
        Implementing classes must define this method.
        """
        pass
