from functools import wraps
from typing import Any, Callable


def log_command(command_name: str) -> Callable:
    """Decorator that prints simple command logs to the terminal."""

    def decorator(function: Callable) -> Callable:
        @wraps(function)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"Command started: {command_name}")
            result = await function(*args, **kwargs)
            print(f"Command finished: {command_name}")
            return result

        return wrapper

    return decorator
