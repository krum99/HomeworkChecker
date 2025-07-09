import os
import sys
from types import ModuleType
import importlib.util
from constants import Path
from data.task_code import TaskCode
from data.homework_test_suite import HomeworkTestSuite


# TODO Refactor, some of these functions should go to utils or build other services.
# TODO Either this should be a specific loader that depends on the TaskCode, either
# it should not depend on it.
class TestLoader:
    """
    A utility class for loading test cases for a specific task based on its TaskCode.

    This class provides static methods to:
    - Parse a TaskCode into its lecture and task components
    - Build the expected path to the corresponding test file
    - Dynamically import the test module and extract the 'test_suite' variable,
      which must be an instance of HomeworkTestSuite
    """

    @staticmethod
    def load(task_code: TaskCode) -> HomeworkTestSuite:
        """
        Loads the test suite for the given TaskCode.

        Parameters:
            task_code (TaskCode): Parsed task code object (e.g., representing 'L2_T3').

        Returns:
            HomeworkTestSuite: The test suite defined in the corresponding test module.

        Raises:
            SystemExit: If the test file is not found or does not define 'test_suite'.
        """
        test_path = TestLoader._build_test_path(task_code.get_lecture(), task_code.get_task())
        module = TestLoader._import_test_module(test_path)

        if not hasattr(module, "test_suite"):
            print(f"No 'test_cases' defined in {test_path}")
            sys.exit(1)

        return module.test_suite

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

