#!/usr/bin/env python3

import alchemy


def main() -> None:
    print("=== Alembic 1 ====")
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air:", end=" ")
    print(alchemy.create_air())
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing create_earth:", end=" ")
    print(alchemy.create_earth())


if __name__ == "__main__":
    main()
