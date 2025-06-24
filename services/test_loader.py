import os
import sys
from types import ModuleType
import importlib.util
from constants import Path

class TestLoader:
    """
    A utility class for loading test cases for a specific task based on its task code.

    The class provides static methods to:
    - Parse a task code (e.g., 'L2_T3') into its components
    - Build the expected path to the corresponding test file
    - Dynamically import the test module and extract the 'test_cases' variable
    """

    @staticmethod
    def load(task_code: str) -> list[tuple[str, list[str], str]]:
        """
        Loads the list of test cases for the given task code.

        Parameters:
            task_code (str): A string in the format 'L<number>_T<number>', e.g. 'L2_T3'.

        Returns:
            list: A list of test cases defined in the corresponding test module.

        Raises:
            SystemExit: If the test file is not found or does not define 'test_cases'.
        """
        level, task = task_code.split("_")
        test_path = TestLoader._build_test_path(level, task)
        module = TestLoader._import_test_module(test_path)

        if not hasattr(module, "test_cases"):
            print(f"No 'test_cases' defined in {test_path}")
            sys.exit(1)

        return module.test_cases

    @staticmethod
    def _build_test_path(level: str, task: str) -> str:
        """
        Constructs the file path to the test module for the given level and task.

        Parameters:
            level (str): The lecture identifier, e.g. 'L2'.
            task (str): The task identifier, e.g. 'T3'.

        Returns:
            str: The file path to the test module.

        Raises:
            SystemExit: If the test file does not exist.
        """
        test_path = os.path.join(Path.TESTS_DIR, level, task + ".py")
        if not os.path.exists(test_path):
            print(f"Test file not found: {test_path}")
            sys.exit(1)
        return test_path

    @staticmethod
    def _import_test_module(test_path: str) -> ModuleType:
        """
        Dynamically imports the test module from the given path.

        Parameters:
            test_path (str): The file path to the test module.

        Returns:
            module: The imported Python module.
        """
        spec = importlib.util.spec_from_file_location("test_module", test_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

