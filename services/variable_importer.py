

from typing import Any
from interfaces.base_importer import BaseImporter


class VariableImporter(BaseImporter):
    def import_object(self, path: str, name: str) -> Any:
        module = self._import_module(path)
        if not hasattr(module, name):
            raise ImportError(f"Variable '{name}' not found in module: {path}")
        return getattr(module, name)
