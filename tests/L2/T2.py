from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_cases = [
    HomeworkTestCase("Lowercase anagram", ["listen", "silent"], "True"),
    HomeworkTestCase("Case-insensitive anagram", ["Elvis", "Lives"], "True"),
    HomeworkTestCase("Phrases with spaces", ["rocket boys", "october sky"], "True"),
    HomeworkTestCase("Not anagrams", ["hello", "world"], "False"),
    HomeworkTestCase("Same letters, different count", ["aabb", "ab"], "False"),
]

test_suite = HomeworkTestSuite(test_cases)
