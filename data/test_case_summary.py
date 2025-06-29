from data.homework_test_case import HomeworkTestCase


class TestCaseSummary:
    def __init__(self, test_case: HomeworkTestCase, output: str):
        self._test_case = test_case
        self._output = output

    def get_test_case(self) -> HomeworkTestCase:
        return self._test_case

    def get_output(self) -> str:
        return self._output

    def is_passed(self) -> bool:
        return self._output.strip() == self._test_case.get_expected_output().strip()

    def __str__(self) -> str:
        status = "✅ PASSED" if self.is_passed() else "❌ FAILED"
        return (
            f"{str(self._test_case)}\n"
            f"⬅️ Output received: {self._output.strip()}\n"
            f"{status}\n"
        )
