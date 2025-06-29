from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Positive exponent", ["2", "10"], "1024"),
    HomeworkTestCase("Zero exponent", ["7", "0"], "1"),
    HomeworkTestCase("Exponent of 1", ["123", "1"], "123"),
    HomeworkTestCase("Base 1 with large exponent", ["1", "100"], "1"),
    HomeworkTestCase("Negative base with even exponent", ["-2", "4"], "16"),
]

test_suite = HomeworkTestSuite(test_cases)
