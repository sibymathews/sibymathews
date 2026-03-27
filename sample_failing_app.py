#!/usr/bin/env python3
"""
POC: intentionally logs secret-like values and then fails.
Do NOT copy patterns like this into real code.
"""

import json
import os
import sys
import time
import traceback


def log(msg: str):
    print(f"[INFO] {time.strftime('%Y-%m-%d %H:%M:%S')} {msg}")


def log_error(msg: str):
    print(f"[ERROR] {time.strftime('%Y-%m-%d %H:%M:%S')} {msg}", file=sys.stderr)


def main():
    log("Starting CM Build Triage Agent POC sample app")

    # Fake secrets - for scanner validation only
    password = os.getenv("DB_PASSWORD", "Welcome1!")
    token = os.getenv("AUTH_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.FAKE.PAYLOAD")
    api_key = os.getenv("API_KEY", "AKIAFAKEKEY1234567890")

    # Intentionally BAD: printing secrets
    log(f"Connecting to DB with password={password}")
    log(f"Authorization: Bearer {token}")
    log(json.dumps({"username": "cm_user", "password": password, "api_key": api_key}))

    # Simulate some processing
    log("Running step: parse_config")
    cfg = {"retries": 3, "timeout": "30"}  # timeout should be int, will cause failure below

    log("Running step: compute_timeout")
    # Intentional bug: comparing string to int (TypeError)
    if cfg["timeout"] > 10:
        log("Timeout is large")

    # Another failure path (won't be reached)
    value = None
    log(f"Length is {len(value)}")

    log("Completed successfully (should not happen)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_error("Unhandled exception occurred")
        traceback.print_exc()
        sys.exit(1)