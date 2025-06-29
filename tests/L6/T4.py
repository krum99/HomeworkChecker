from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Simple palindrome", ["madam"], "True"),
    HomeworkTestCase("Single character", ["a"], "True"),
    HomeworkTestCase("Not a palindrome", ["hello"], "False"),
    HomeworkTestCase("Even-length palindrome", ["noon"], "True"),
    HomeworkTestCase("Case-sensitive non-palindrome", ["Madam"], "False"),
]

test_suite = HomeworkTestSuite(test_cases)
