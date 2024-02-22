class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, template: str = f"[INFO]: "):
        self._template = template

    def log(self, message):
        print(f"{self._template} {message}")
