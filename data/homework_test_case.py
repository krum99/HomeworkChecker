class HomeworkTestCase:
    def __init__(self, description: str, args: list[str], expected_output: str, stdin: bool = False):
        self._description = description
        self._args = args
        self._expected_output = expected_output
        self._stdin = stdin

    # Getters
    def get_description(self) -> str:
        return self._description

    def get_args(self) -> list[str]:
        return self._args

    def get_expected_output(self) -> str:
        return self._expected_output

    def is_stdin(self) -> bool:
        return self._stdin

    def __str__(self) -> str:
        args_str = " ".join(self._args)
        return (
            f"🧪 {self._description}\n"
            f"➡️ Running with arguments: {args_str}\n"
            f"📥 Expected output: {self._expected_output}"
        )
