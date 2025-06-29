import sys
from data.test_case_summary import TestCaseSummary
from data.test_suite_summary import TestSuiteSummary
from utils import run_test
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

    results: list[TestCaseSummary] = []

    for test in test_suite:
        summary = run_test(script_file, test)
        results.append(summary)

    # # TODO Refactor!
    # # L10_T1 check
    # expected_content = "apple\nbanana\ncherry"

    # if task_code == TaskCode.from_string("_L10_T1"):
    #     with open("tests/assets/sorted_output.txt") as f:
    #         actual = f.read().strip()
    #     return actual == expected_content

    test_suite_summary = TestSuiteSummary(results)
    print(test_suite_summary)

if __name__ == "__main__":
    run()

