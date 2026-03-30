import subprocess
import os
import re
from pathlib import Path

def run_tests_and_export_outputs(docs_folder="../docs", output_folder="outputs"):
    """
    Run all test files in `docs_folder`, capture print outputs per test case,
    and export them to a corresponding .txt file in `output_folder`.
    Each test's output is separated by section markers.
    """
    # Ensure output folder exists
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    docs_folder = Path(docs_folder)
    print(f"Finding test in folder {docs_folder}")
    for test_file in docs_folder.rglob("*.py"):

        print(f"Processing {test_file.name}")
        if test_file.name == "conftest.py":
            continue

        # Determine the output file name
        output_file = test_file.with_suffix(".txt")

        # Run pytest for the current test file and capture output
        result = subprocess.run(
            ["pytest", test_file, "-s", "-p no:terminal", "--capture=tee-sys"],
            capture_output=True,
            text=True,
            check=False,
        )

        with open(output_file, "w") as f:
            f.write(result.stdout)


if __name__ == "__main__":
    run_tests_and_export_outputs()