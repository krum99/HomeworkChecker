from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Basic Caesar shift", ["abc", "1"], "bcd"),
    HomeworkTestCase("Wrap around from 'z' to 'a'", ["xyz", "3"], "abc"),
    HomeworkTestCase("Upper and lower case mixed", ["AbC", "2"], "CdE"),
    HomeworkTestCase("With non-alphabetic characters", ["Hello, World!", "5"], "Mjqqt, Btwqi!"),
    HomeworkTestCase("Negative shift", ["bcd", "-1"], "abc"),
]

test_suite = HomeworkTestSuite(test_cases)
