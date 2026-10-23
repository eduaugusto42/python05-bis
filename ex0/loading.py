#!/usr/bin/env python3

import importlib.metadata


def get_version(reagent: str) -> str | None:
    try:
        return importlib.metadata.version(reagent)
    except importlib.metadata.PackageNotFoundError:
        return None


def main() -> None:
    reagents: list[str] = ["pandas", "numpy"]

    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")
    print()

    all_ok: bool = True

    for reagent in reagents:
        version = get_version(reagent)
        if version is None:
            all_ok = False
            print(f"[ ] {reagent} - not installed")
            print(f"    Install with pip: pip install {reagent}")
            print(f"    Install with poetry: poetry add {reagent}")
            continue

        if reagent == "pandas":
            print(f"[OK] {reagent} ({version}) - Data manipulation ready")
        elif reagent == "numpy":
            print(f"[OK] {reagent} ({version}) - Numerical computation ready")

    print("pip vs Poetry:")
    print(
        "   requirements.txt declares what to install;"
        " pip resolves it at install time."
    )
    print(
        "   pyproject.toml declares the same constraints,"
        " and Poetry pins the resolved versions in poetry.lock"
        " so every install is identical."
    )

    if all_ok:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
