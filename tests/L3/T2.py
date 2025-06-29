from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Simple lowercase", ["attackatdawn", "lemon"], "lxfopvefrnhr"),
    HomeworkTestCase("Mixed case", ["AttackAtDawn", "LEMON"], "LxfopvEfRnhr"),
    HomeworkTestCase("Short key repeated", ["hello", "a"], "hello"),
    HomeworkTestCase("Wrap-around key", ["xyz", "abc"], "xza"),
    HomeworkTestCase("With non-letter characters", ["Hi there!", "key"], "Rm xlivi!"),
]

test_suite = HomeworkTestSuite(test_cases)
