from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Simple lowercase string", ["bananalilac"], "[('a', 5), ('b', 1), ('c', 1), ('i', 1), ('l', 2), ('n', 1)]"),
    HomeworkTestCase("Empty input", [""], "[]"),
    HomeworkTestCase("All identical characters", ["aaaaa"], "[('a', 5)]"),
    HomeworkTestCase("Case-sensitive input", ["AaA"], "[('A', 2), ('a', 1)]"),
    HomeworkTestCase("Includes whitespace and punctuation", ["a b!b a"], "[('a', 2), (' ', 2), ('b', 2), ('!', 1)]"),
]

test_suite = HomeworkTestSuite(test_cases)
