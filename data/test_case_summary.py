from data.homework_test_case import HomeworkTestCase


class TestCaseSummary:
    """
    Represents the result of executing a single test case against a student solution.

    This class stores both the test case definition and the actual output produced by the solution.
    It provides methods to check if the test passed and to retrieve related data.
    """

    def __init__(self, test_case: HomeworkTestCase, output: str):
        """
        Initializes the summary with the executed test case and the output it produced.

        Args:
            test_case (HomeworkTestCase): The test case that was executed.
            output (str): The actual output returned by the student solution.
        """
        self._test_case = test_case
        self._output = output

    def get_test_case(self) -> HomeworkTestCase:
        """
        Returns the test case associated with this result.

        Returns:
            HomeworkTestCase: The test case object.
        """
        return self._test_case

    def get_output(self) -> str:
        """
        Returns the actual output received from the student solution.

        Returns:
            str: The raw output as returned by the script.
        """
        return self._output

    def is_passed(self) -> bool:
        """
        Determines whether the output matches the expected result.

        Returns:
            bool: True if the test passed, False otherwise.
        """
        return self._output.strip() == self._test_case.get_expected_output().strip()

    def __str__(self) -> str:
        """
        Returns a string representation of the test result, including the test case description,
        the output received, and a pass/fail status.

        Returns:
            str: A formatted string showing the result of the test.
        """
        status = "✅ PASSED" if self.is_passed() else "❌ FAILED"
        return (
            f"{str(self._test_case)}\n"
            f"⬅️ Output received: {self._output.strip()}\n"
            f"{status}\n"
        )

