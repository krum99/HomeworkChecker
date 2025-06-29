from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Ascending integers", ["1", "2", "3"], "sorted"),
    HomeworkTestCase("Repeated values in order", ["1", "2", "2"], "sorted"),
    HomeworkTestCase("Descending order", ["3", "2", "1"], "unsorted"),
    HomeworkTestCase("Negative numbers sorted", ["-3", "-2", "-1"], "sorted"),
    HomeworkTestCase("Negative numbers unsorted", ["-1", "-3", "-2"], "unsorted"),
    HomeworkTestCase("Single element", ["42"], "sorted"),
    HomeworkTestCase("Empty list", [], "sorted"),
    HomeworkTestCase("Strings sorted alphabetically", ["a", "b", "c"], "sorted"),
    HomeworkTestCase("Strings unsorted", ["b", "a"], "unsorted"),
    HomeworkTestCase("Mixed digits as strings", ["1", "10", "2"], "unsorted"),
]

test_suite = HomeworkTestSuite(test_cases)
