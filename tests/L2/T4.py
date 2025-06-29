from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Repeated numbers", ["6", "3", "7", "4", "7", "4", "7", "4", "8", "4", "3", "8", "4", "3", "8", "3", "9", "4", "3"], "[3, 4, 6, 7, 8, 9]"),
    HomeworkTestCase("No duplicates", ["1", "2", "3"], "[1, 2, 3]"),
    HomeworkTestCase("All same number", ["5", "5", "5", "5"], "[5]"),
    HomeworkTestCase("Empty list", [], "[]"),
    HomeworkTestCase("Mixed order with repeats", ["10", "2", "10", "3", "2", "3", "1"], "[1, 2, 3, 10]"),
]

test_suite = HomeworkTestSuite(test_cases)
