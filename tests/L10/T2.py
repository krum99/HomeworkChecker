from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Match stem 'walking'", ["tests/assets/stems.txt", "walking"], "walk"),
    HomeworkTestCase("Match stem 'ran'", ["tests/assets/stems.txt", "ran"], "run"),
]

test_suite = HomeworkTestSuite(test_cases)
