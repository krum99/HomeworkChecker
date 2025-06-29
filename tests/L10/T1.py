from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite
import os

# Clean-up before running
if os.path.exists("tests/assets/sorted_output.txt"):
    os.remove("tests/assets/sorted_output.txt")

test_suite = HomeworkTestSuite([
    HomeworkTestCase(
        description="Sort lines from file",
        args=["tests/assets/unsorted.txt", "tests/assets/sorted_output.txt"],
        expected_output=""  # No console output expected
    )
])