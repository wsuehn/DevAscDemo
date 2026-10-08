def greet(name: str) -> str:
    """Return a simple greeting message."""
    return f"Hello, {name}! Welcome to the feature."


def add_numbers(first: int, second: int) -> int:
    """Add two numbers together."""
    return first + second


if __name__ == "__main__":
    print(greet("Developer"))
    print(add_numbers(5, 7))
    print("This is a feature module that can be imported into other scripts.")
