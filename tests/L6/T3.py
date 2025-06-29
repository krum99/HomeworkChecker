from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Existing element in the middle", ["584"], "found at 54"),
    HomeworkTestCase("Element not found", ["99999"], "not found"),
    HomeworkTestCase("First element", ["30"], "found at 0"),
    HomeworkTestCase("Last element", ["988"], "found at 77"),
    HomeworkTestCase("Duplicate value - finds first", ["521"], "found at 46"),
]

test_suite = HomeworkTestSuite(test_cases)
