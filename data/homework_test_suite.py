from data.homework_test_case import HomeworkTestCase

class HomeworkTestSuite:
    def __init__(self, test_cases: list[HomeworkTestCase]):
        self._test_cases = test_cases

    def __len__(self) -> int:
        return len(self._test_cases)

    def __iter__(self):
        return iter(self._test_cases)