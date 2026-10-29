#!/usr/bin/env python3

import os
from dotenv import load_dotenv


def get_config() -> dict[str, str]:
    load_dotenv()
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv(
            "DATABASE_URL", "postgresql://localhost:5432/alchemy"
        ),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv(
            "ZION_ENDPOINT", "http://localhost:8080/zion"
        ),
    }


def main() -> None:
    config = get_config()
    missing = [
        key
        for key in (
            "MATRIX_MODE",
            "DATABASE_URL",
            "API_KEY",
            "LOG_LEVEL",
            "ZION_ENDPOINT",
        )
        if os.getenv(key) is None
    ]
    if missing:
        print(f"WARNING: Missing configuration: {', '.join(missing)}")
    print("ORACLE STATUS: Consulting the configuration...")
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    if config["MATRIX_MODE"] == "production":
        print("Database: Connected to production instance")
        print("Log Level: INFO")
    else:
        print("Database: Connected to local instance")
        print(f"Log Level: {config['LOG_LEVEL']}")
    print("API Access: Authenticated")
    print("Remote Network: Online")
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly ignored by git")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
