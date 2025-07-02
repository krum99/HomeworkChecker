import subprocess
import sys
from data.homework_test_case import HomeworkTestCase
from data.test_case_summary import TestCaseSummary

def run_solution_file(script_file: str, *args: str) -> str:
    """
    Executes a Python script as a subprocess, passing arguments via command line.

    This function launches the given Python file using the current interpreter (sys.executable),
    and passes all provided arguments as strings to the script. The standard output is captured
    and returned as a trimmed string. Standard error is ignored unless handled explicitly elsewhere.

    Parameters:
        script_file (str): Path to the Python script to execute.
        *args (str): Positional arguments (as strings) to be passed to the script.

    Returns:
        str: The script's stdout, with leading/trailing whitespace removed.

    Example:
        >>> run_solution_file("F12345_L2_T3.py", "1", "2", "3")
        'False'

        >>> run_solution_file("script.py")
        'Hello world'

    Note:
        All arguments are passed as strings. If the student's script expects integers or floats,
        it should convert them internally (e.g., using int() or float()).
    """
    result = subprocess.run(
        [sys.executable, script_file] + list(args),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()

def run_test(script_file: str, test_case: HomeworkTestCase) -> TestCaseSummary:
    """
    Executes a single test case against a student solution script.

    This function:
        - Runs the student's Python file using the provided input arguments
        - Captures and stores the output
        - Compares it to the expected result
        - Wraps both input and output into a TestCaseSummary instance

    Parameters:
        script_file (str): Path to the student's solution file (e.g., 'F12345_L2_T3.py').
        test_case (HomeworkTestCase): A test case with description, arguments, and expected output.

    Returns:
        TestCaseSummary: A summary object containing the input test case and actual output,
                         with a method to check if the test passed.

    Example:
        >>> test = HomeworkTestCase("Duplicate input", ["1", "2", "2"], "True")
        >>> summary = run_test("F12345_L2_T3.py", test)
        >>> print(summary.is_passed())
        True
    """
    output = run_solution_file(script_file, *test_case.get_args())

    return TestCaseSummary(test_case, output)
