"""Greeter CLI entry point."""


import argparse
from datetime import datetime


def greet(name: str, verbose: bool = False) -> str:
    """Return a greeting for the given name."""
    message = f"Hello, {name}!!"
    if verbose:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message += f" (Current time: {now})"
    return message


def main() -> None:
    """Run the greeter CLI."""
    parser = argparse.ArgumentParser(description="A friendly greeter")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    parser.add_argument("-v", "--verbose", action="store_true", help="Include current time")
    args = parser.parse_args()
    print(greet(args.name, args.verbose))


if __name__ == "__main__":
    main()
