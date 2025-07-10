from interfaces.base_importer import BaseImporter


class ClassImporter(BaseImporter):
    def import_object(self, path: str, name: str) -> type:
        module = self._import_module(path)
        obj = getattr(module, name, None)
        if obj is None:
            raise ImportError(f"Class '{name}' not found in module: {path}")
        if not isinstance(obj, type):
            raise TypeError(f"'{name}' in {path} is not a class")
        return obj
