import importlib.util
import subprocess
import sys
import os
import re
from constants import Path, Pattern

def extract_task_code(filename):
    """
    Extracts the task identifier from a student solution filename.

    The expected filename format is: FXXXXX_Ln_Tm.py, where:
        - FXXXXX is the student ID or prefix (ignored)
        - Ln is the homework (e.g., L2)
        - Tm is the task number (e.g., T3)

    The function returns the string "Ln_Tm" (e.g., "L2_T3").

    Parameters:
        filename (str): The name of the solution file.

    Returns:
        str: The extracted task code in the format "L<number>_T<number>".

    Raises:
        SystemExit: If the task code cannot be found in the filename.

    Example:
        >>> extract_task_code("F12345_L2_T3.py")
        'L2_T3'

        >>> extract_task_code("solution_L1_T5.py")
        'L1_T5'

        >>> extract_task_code("invalid_name.py")
        Could not extract task code from filename: invalid_name.py
        (then exits the program)
    """
    match = re.search(Pattern.TASK_CODE, filename)
    if not match:
        print(f"Could not extract task code from filename: {filename}")
        sys.exit(1)
    return match.group(0)[1:]

def load_test_cases(task_code):
    """
    Dynamically loads the list of test cases for a given task.

    Given a task code in the format "L<number>_T<number>", this function constructs the expected
    file path of the test definition module (e.g., "tests/L2/T3.py"), dynamically imports it,
    and returns the `test_cases` variable defined within.

    Parameters:
        task_code (str): Task identifier in the format "L<number>_T<number>", e.g., "L2_T3".

    Returns:
        list: The list of test cases defined as `test_cases` in the corresponding file.

    Raises:
        SystemExit: If the test file is not found or does not contain `test_cases`.

    Example:
        >>> load_test_cases("L2_T3")
        [
            ("Description 1", ["1", "1"], "True"),
            ("Description 2", ["1", "2"], "False"),
            ...
        ]

    Directory structure expected:
        - tests/
          └── L2/
              └── T3.py  # Contains a `test_cases = [...]` variable
    """
    level, task = task_code.split("_")
    
    test_path = os.path.join(Path.TESTS_DIR, level, task + ".py")
    if not os.path.exists(test_path):
        print(f"Test file not found: {test_path}")
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("test_module", test_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "test_cases"):
        print(f"No 'test_cases' defined in {test_path}")
        sys.exit(1)

    return module.test_cases

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

def run_test(script_file, description, args, expected_output):
    """
    Runs a single test case against a given student solution script and prints the result.

    This function:
        - Executes the target Python script with the provided arguments
        - Compares the actual output to the expected output
        - Prints a formatted message indicating success or failure
        - Returns True if the output matches, otherwise False

    Parameters:
        script_file (str): Path to the student's solution file to be executed.
        description (str): Human-readable description of the test case.
        args (list of str): Command-line arguments to pass to the script.
        expected_output (str): The output that the script is expected to produce.

    Returns:
        bool: True if the output matches the expected output, False otherwise.

    Example:
        >>> run_test("F12345_L2_T3.py", "Duplicate input", ["1", "2", "2"], "True")
        🧪 Duplicate input
        ➡️ Running with arguments: 1 2 2
        ⬅️ Output received: True
        ✅ Test passed
        True
    """
    print(f"🧪 {description}")
    print(f"➡️ Running with arguments: {' '.join(args)}")
    output = run_solution_file(script_file, *args)
    print(f"⬅️ Output received: {output}")
    if output == expected_output:
        print("✅ Test passed\n")
        return True
    else:
        print(f"❌ Test failed – expected: {expected_output}\n")
        return False