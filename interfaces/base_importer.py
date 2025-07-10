from abc import ABC, abstractmethod
from types import ModuleType
import importlib.util
from typing import Any


class BaseImporter(ABC):
    def _import_module(self, path: str, module_name: str = "dynamic_module") -> ModuleType:
        spec = importlib.util.spec_from_file_location(module_name, path)
        if not spec or not spec.loader:
            raise ImportError(f"Cannot load module from {path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    @abstractmethod
    def import_object(self, path: str, name: str) -> Any:
        pass
