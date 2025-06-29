import re
from constants import Pattern

class TaskCode:
    """
    Represents a parsed task code in the format 'L<number>_T<number>'.

    This class is responsible for extracting and holding the lecture and task identifiers from a given string,
    such as a filename like 'F12345_L2_T3.py'. It supports access to the individual parts (lecture and task)
    and provides a factory method for construction from a raw string.
    """

    def __init__(self, lecture: str, task: str):
        """
        Initializes a TaskCode instance with the given lecture and task components.

        Args:
            lecture (str): The lecture code (e.g., "L2").
            task (str): The task code (e.g., "T3").
        """
        self.lecture = lecture
        self.task = task

    @classmethod
    def from_string(cls, raw: str) -> "TaskCode":
        """
        Creates a TaskCode instance by extracting the task code from a raw string.

        The raw string should contain a substring matching the pattern '_L<number>_T<number>',
        such as a filename like 'F12345_L2_T3.py'.

        Args:
            raw (str): A string containing the task code.

        Returns:
            TaskCode: A new instance with the extracted lecture and task values.

        Raises:
            ValueError: If no valid task code can be found in the input string.

        Example:
            >>> TaskCode.from_string("F12345_L2_T3.py")
            TaskCode(lecture="L2", task="T3")
        """
        match = re.search(Pattern.TASK_CODE, raw)
        if not match:
            raise ValueError(f"Invalid task code in string: {raw}")
        code = match.group(0)[1:]  # remove leading "_"
        level, task = code.split("_")
        return cls(level, task)

    def get_lecture(self) -> str:
        """
        Returns the lecture component of the task code.

        Returns:
            str: The lecture part, e.g., "L2".
        """
        return self.lecture

    def get_task(self) -> str:
        """
        Returns the task component of the task code.

        Returns:
            str: The task part, e.g., "T3".
        """
        return self.task


