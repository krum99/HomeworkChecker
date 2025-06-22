import importlib.util
import subprocess
import sys
import os

def load_test_cases(task_code):
    level, task = task_code.split("_")
    test_path = f"tests/{level}/{task}.py"
    if not os.path.exists(test_path):
        print(f"❌ Test file not found: {test_path}")
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("test_module", test_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "test_cases"):
        print(f"❌ No 'test_cases' defined in {test_path}")
        sys.exit(1)

    return module.test_cases

def run_solution_file(script_file, *args):
    result = subprocess.run(
        [sys.executable, script_file] + list(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()

def run_test(script_file, args, expected_output):
    print(f"➡️ Running test with arguments: {' '.join(args)}")
    output = run_solution_file(script_file, *args)
    print(f"⬅️ Output received: {output}")
    if output == expected_output:
        print("✅ Test passed\n")
        return True
    else:
        print(f"❌ Test failed – expected: {expected_output}\n")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python runner.py <solution_file.py> <task_code>")
        print("Example: python runner.py F12345_L2_T3.py L2_T3")
        sys.exit(1)

    script_file = sys.argv[1]
    task_code = sys.argv[2]

    test_cases = load_test_cases(task_code)

    passed = 0
    total = len(test_cases)

    for args, expected in test_cases:
        if run_test(script_file, args, expected):
            passed += 1

    print("📊 Test Summary:")
    print(f"✅ Passed:   {passed}/{total}")
    print(f"❌ Failed:   {total - passed}/{total}")
    if passed == total:
        print("🎉 All tests passed successfully!")
    else:
        print("⚠️ Some tests failed. Please review your solution.")
