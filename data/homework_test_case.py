class HomeworkTestCase:
    """
    Represents a single test case for a student's homework task.

    This class encapsulates a test description, a list of command-line arguments,
    and the expected output. It is designed to be used by test runners or frameworks
    that evaluate student Python scripts by executing them with given parameters and
    comparing the result to the expected value.

    Attributes:
        _description (str): Human-readable explanation of what the test verifies.
        _args (list[str]): List of command-line arguments to pass to the student's script.
        _expected_output (str): Expected output that should be produced by the script.
    """

    def __init__(self, description: str, args: list[str], expected_output: str):
        """
        Initializes a new HomeworkTestCase.

        Args:
            description (str): Description of the test case.
            args (list[str]): Command-line arguments for the student solution.
            expected_output (str): Expected output string.
        """
        self._description = description
        self._args = args
        self._expected_output = expected_output

    def get_description(self) -> str:
        """
        Returns the description of the test case.

        Returns:
            str: Description of the test.
        """
        return self._description

    def get_args(self) -> list[str]:
        """
        Returns the list of command-line arguments for the test.

        Returns:
            list[str]: List of arguments to be passed to the script.
        """
        return self._args

    def get_expected_output(self) -> str:
        """
        Returns the expected output for this test case.

        Returns:
            str: The expected string output.
        """
        return self._expected_output

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the test case.

        Returns:
            str: A multi-line string showing the description, input arguments,
                 and expected output.
        """
        args_str = " ".join(self._args)
        return (
            f"🧪 {self._description}\n"
            f"➡️ Running with arguments: {args_str}\n"
            f"📥 Expected output: {self._expected_output}"
        )
