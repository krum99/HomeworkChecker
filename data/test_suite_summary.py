


from data.test_case_summary import TestCaseSummary


class TestSuiteSummary:
    def __init__(self, summaries: list[TestCaseSummary]):
        self._summaries = summaries

    def get_summaries(self) -> list[TestCaseSummary]:
        return self._summaries

    def get_total(self) -> int:
        return len(self._summaries)

    def get_passed_count(self) -> int:
        return sum(1 for summary in self._summaries if summary.is_passed())

    def get_failed_count(self) -> int:
        return self.get_total() - self.get_passed_count()

    def all_passed(self) -> bool:
        return self.get_passed_count() == self.get_total()

    def __str__(self) -> str:
        result_lines = [str(summary) for summary in self._summaries]
        summary_line = (
            f"\n📊 Test Summary:\n"
            f"✅ Passed:   {self.get_passed_count()}/{self.get_total()}\n"
            f"❌ Failed:   {self.get_failed_count()}/{self.get_total()}"
        )
        if self.all_passed():
            summary_line += "\n🎉 All tests passed successfully!"
        return "\n".join(result_lines) + summary_line