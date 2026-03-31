import subprocess

from pathlib import Path
from typing import Annotated

import typer

def export_test_outputs(
        docs_folder: Annotated[str, typer.Argument(help="Folder in which to search for Python files.")] = "../docs"):
    """
    Run all test files in `docs_folder`, capture print outputs per test case,
    and export them to a corresponding .txt file in `output_folder`.
    Each test's output is separated by section markers.
    """

    docs_folder = Path(docs_folder)
    print(f"Finding tests in folder {docs_folder}")
    files = list(docs_folder.rglob("*.py"))
    if len(files) == 0:
        print("No tests found in folder")
    for test_file in files:
        print(f"Exporting {test_file.name}... ".ljust(40), end="")
        if test_file.name == "conftest.py":
            print("Skipping...")
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

        print(f"Found and ran {len(result.stdout.split('--8<-- [start')) - 1} tests... ".ljust(40), end="")

        with open(output_file, "w") as f:
            f.write(result.stdout)

        print(f"Finished writing to {output_file}")

if __name__ == "__main__":
    typer.run(export_test_outputs)
