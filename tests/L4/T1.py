from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Find keys for value 'a'", ["a"], "[1, 4, 7]"),
    HomeworkTestCase("Find keys for value 'b'", ["b"], "[2, 8]"),
    HomeworkTestCase("Find keys for value 'c'", ["c"], "[3]"),
    HomeworkTestCase("Find keys for value 'd'", ["d"], "[5]"),
    HomeworkTestCase("Value not in dictionary", ["z"], "[]"),
]

test_suite = HomeworkTestSuite(test_cases)
