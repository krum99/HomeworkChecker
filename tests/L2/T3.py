test_cases = [
    ("Duplicate at the beginning", ["5", "3", "1", "5", "9", "2", "8", "6", "7"], "True"),
    ("All elements are unique", ["1", "2", "3", "4", "5"], "False"),
    ("Empty list", [], "False"),
    ("Two identical elements", ["1", "1"], "True"),
    ("Negative numbers with a duplicate", ["-1", "-2", "-3", "-1"], "True"),
    ("All zeros", ["0", "0", "0"], "True"),
    ("Only one element", ["42"], "False")
]
