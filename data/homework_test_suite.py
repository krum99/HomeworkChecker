from data.homework_test_case import HomeworkTestCase

class HomeworkTestSuite:
    """
    Represents a collection of test cases for a given homework task.

    A HomeworkTestSuite encapsulates multiple HomeworkTestCase instances and provides
    iterable and length behavior to facilitate batch test execution and summary reporting.

    Attributes:
        _test_cases (list[HomeworkTestCase]): The list of test cases included in the suite.
    """

    def __init__(self, test_cases: list[HomeworkTestCase]):
        """
        Initializes a new HomeworkTestSuite.

        Args:
            test_cases (list[HomeworkTestCase]): A list of test cases to be included in the suite.
        """
        self._test_cases = test_cases

    def __len__(self) -> int:
        """
        Returns the number of test cases in the suite.

        Returns:
            int: The total number of test cases.
        """
        return len(self._test_cases)

    def __iter__(self):
        """
        Returns an iterator over the test cases in the suite.

        Returns:
            Iterator[HomeworkTestCase]: An iterator over the contained test cases.
        """
        return iter(self._test_cases)
