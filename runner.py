import sys
from utils import run_test
from services.test_loader import TestLoader
from data.task_code import TaskCode
from data.homework_test_case import HomeworkTestCase

def run():
    if len(sys.argv) != 2:
        print("Usage: python runner.py <solution_file.py>")
        print("Example: python runner.py F123456_L2_T3.py")
        sys.exit(1)

    script_file = sys.argv[1]

    task_code = TaskCode.from_string(script_file)
    
    test_cases = TestLoader.load(task_code)

    passed = 0
    total = len(test_cases)

    for test in test_cases:
        if run_test(script_file, test):
            passed += 1

    print("📊 Test Summary:")
    print(f"✅ Passed:   {passed}/{total}")
    print(f"❌ Failed:   {total - passed}/{total}")
    if passed == total:
        print("🎉 All tests passed successfully!")
    else:
        print("⚠️ Some tests failed. Please review your solution.")

if __name__ == "__main__":
    run()

