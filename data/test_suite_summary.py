


from data.test_case_summary import TestCaseSummary

class TestSuiteSummary:
    """
    Represents a summary of the results of executing an entire test suite.

    This class aggregates the results of individual test cases and provides statistics such as 
    the number of passed/failed tests, whether all tests passed, and a string representation 
    of the full summary.
    """

    def __init__(self, summaries: list[TestCaseSummary]):
        """
        Initializes the test suite summary with a list of individual test case summaries.

        Args:
            summaries (list[TestCaseSummary]): A list of results from individual test executions.
        """
        self._summaries = summaries

    def get_summaries(self) -> list[TestCaseSummary]:
        """
        Returns all individual test case summaries.

        Returns:
            list[TestCaseSummary]: The list of results per test case.
        """
        return self._summaries

    def get_total(self) -> int:
        """
        Returns the total number of test cases in the suite.

        Returns:
            int: Total number of executed tests.
        """
        return len(self._summaries)

    def get_passed_count(self) -> int:
        """
        Returns the number of passed test cases.

        Returns:
            int: Number of successful test cases.
        """
        return sum(1 for summary in self._summaries if summary.is_passed())

    def get_failed_count(self) -> int:
        """
        Returns the number of failed test cases.

        Returns:
            int: Number of failed test cases.
        """
        return self.get_total() - self.get_passed_count()

    def all_passed(self) -> bool:
        """
        Checks if all test cases passed.

        Returns:
            bool: True if all tests passed, False otherwise.
        """
        return self.get_passed_count() == self.get_total()

    def __str__(self) -> str:
        """
        Returns a formatted string containing a detailed report for each test case
        followed by an overall summary.

        Returns:
            str: Human-readable summary of the full test suite execution.
        """
        result_lines = [str(summary) for summary in self._summaries]
        summary_line = (
            f"\n📊 Test Summary:\n"
            f"✅ Passed:   {self.get_passed_count()}/{self.get_total()}\n"
            f"❌ Failed:   {self.get_failed_count()}/{self.get_total()}"
        )
        if self.all_passed():
            summary_line += "\n🎉 All tests passed successfully!"
        return "\n".join(result_lines) + summary_line
