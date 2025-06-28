import subprocess
import sys

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