import os
from constants import Path, FileExtensions
from data.task_code import TaskCode


class HomeworkTestPathBuilder():
    def build_path(self, task_code: TaskCode) -> str:
        lecture = task_code.get_lecture()
        task = task_code.get_task()
        filename = f"{task}{FileExtensions.PYTHON}"
        return os.path.join(Path.TESTS_DIR, lecture, filename)