import os
import sys
from types import ModuleType
import importlib.util
from constants import Path
from data.task_code import TaskCode
from data.homework_test_suite import HomeworkTestSuite
from interfaces.base_importer import BaseImporter
from services.homework_test_path_builder import HomeworkTestPathBuilder


class TestLoader:
    def __init__(self, path_builder: HomeworkTestPathBuilder, importer: BaseImporter, variable_name: str = "test_suite"):
        self.path_builder = path_builder
        self.importer = importer
        self.variable_name = variable_name

    def load(self, task_code: TaskCode) -> HomeworkTestSuite:
        test_path = self.path_builder.build_path(task_code)
        obj = self.importer.import_object(test_path, self.variable_name)

        if not isinstance(obj, HomeworkTestSuite):
            raise TypeError(f"'{self.variable_name}' in {test_path} is not a HomeworkTestSuite")

        return obj
