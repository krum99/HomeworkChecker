import subprocess
import sys
from data.homework_test_case import HomeworkTestCase

def run_solution_file(script_file, *args):
    """
    Executes a Python script with the given command-line arguments and captures its output.

    This function runs the specified script as a subprocess, passing any additional arguments
    as if they were passed via the command line. The standard output of the script is captured
    and returned as a stripped string.

    Parameters:
        script_file (str): Path to the Python script to be executed.
        *args (str): Zero or more arguments to pass to the script via the command line.

    Returns:
        str: The standard output of the executed script, with leading/trailing whitespace removed.

    Example:
        >>> run_solution_file("F12345_L2_T3.py", "1", "2", "3")
        'False'

        >>> run_solution_file("solve.py")
        'special case'
    """
    result = subprocess.run(
        [sys.executable, script_file] + list(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()

def run_test(script_file: str, test_case: HomeworkTestCase) -> bool:
    """
    Runs a single test case against the specified solution script and prints the result.

    This function:
        - Executes the student's Python script with arguments from the HomeworkTestCase
        - Prints a description, input arguments, and actual output
        - Compares the output to the expected result
        - Returns True if the output matches, False otherwise

    Parameters:
        script_file (str): Path to the student solution file.
        test_case (HomeworkTestCase): The test case to run.

    Returns:
        bool: True if the script's output matches the expected output; False otherwise.
    """
    print(test_case)

    output = run_solution_file(script_file, *test_case.get_args())
    print(f"⬅️ Output received: {output}")

    if output == test_case.get_expected_output():
        print("✅ Test passed\n")
        return True
    else:
        print(f"❌ Test failed – expected: {test_case.get_expected_output()}\n")
        return False


def test_summary(total: int, passed: int):
    print("📊 Test Summary:")
    print(f"✅ Passed:   {passed}/{total}")
    print(f"❌ Failed:   {total - passed}/{total}")
    if passed == total:
        print("🎉 All tests passed successfully!")
    else:
        print("⚠️ Some tests failed. Please review your solution.")