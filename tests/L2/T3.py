from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Duplicate at the beginning", ["5", "3", "1", "5", "9", "2", "8", "6", "7"], "True"),
    HomeworkTestCase("All elements are unique", ["1", "2", "3", "4", "5"], "False"),
    HomeworkTestCase("Empty list", [], "False"),
    HomeworkTestCase("Two identical elements", ["1", "1"], "True"),
    HomeworkTestCase("Negative numbers with a duplicate", ["-1", "-2", "-3", "-1"], "True"),
    HomeworkTestCase("All zeros", ["0", "0", "0"], "True"),
    HomeworkTestCase("Only one element", ["42"], "False")
]

test_suite = HomeworkTestSuite(test_cases)