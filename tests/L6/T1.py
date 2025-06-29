from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("From 4 to 10", ["4", "10"], "[2, 3, 5, 8, 13, 21, 34]"),
    HomeworkTestCase("From 0 to 0 (first element)", ["0", "0"], "[0]"),
    HomeworkTestCase("From 0 to 5", ["0", "5"], "[0, 1, 1, 2, 3, 5]"),
    HomeworkTestCase("From 8 to 12", ["8", "12"], "[21, 34, 55, 89, 144]"),
    HomeworkTestCase("From 15 to 15 (single high index)", ["15", "15"], "[610]"),
]

test_suite = HomeworkTestSuite(test_cases)
