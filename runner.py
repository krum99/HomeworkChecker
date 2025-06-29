import sys
from utils import run_test, test_summary
from services.test_loader import TestLoader
from data.task_code import TaskCode

def run():
    if len(sys.argv) != 2:
        print("Usage: python runner.py <solution_file.py>")
        print("Example: python runner.py F123456_L2_T3.py")
        sys.exit(1)

    script_file = sys.argv[1]

    task_code = TaskCode.from_string(script_file)
    
    test_suite = TestLoader.load(task_code)

    passed = 0
    total = len(test_suite)

    for test in test_suite:
        if run_test(script_file, test):
            passed += 1

    # L10_T1 check
    expected_content = "apple\nbanana\ncherry"

    if task_code == TaskCode.from_string("L10_T1"):
        with open("tests/assets/sorted_output.txt") as f:
            actual = f.read().strip()
        return actual == expected_content

    test_summary(total, passed)

if __name__ == "__main__":
    run()

