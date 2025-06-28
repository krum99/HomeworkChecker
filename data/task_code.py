import re
from constants import Pattern

class TaskCode:
    """
    Represents a parsed task code of the form 'L<number>_T<number>'.

    Can be constructed from a full filename (e.g. 'F12312_L2_T3.py') and extracts the valid task code.
    """

    def __init__(self, lecture: str, task: str):
        self.lecture = lecture
        self.task = task

    @classmethod
    def from_string(cls, raw: str) -> "TaskCode":
        match = re.search(Pattern.TASK_CODE, raw)
        if not match:
            raise ValueError(f"Invalid task code in string: {raw}")
        code = match.group(0)[1:]  # remove leading "_"
        level, task = code.split("_")
        return cls(level, task)
    
    def get_lecture(self) -> str:
        return self.lecture

    def get_task(self) -> str:
        return self.task

