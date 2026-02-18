"""Script to convert Jupyter Notebooks to Markdown for documentation.

This script finds all .ipynb files in the examples/ directory, converts them
to Markdown using nbconvert with sanitized filenames, and prints the
configuration snippet for mkdocs.yml.
"""

import shutil
import subprocess
import sys
import re
import pathlib


TEMPLATE_PATH = "mkdocs.tpl"
TEMPLATE_DEST = "share/jupyter/nbconvert/templates"

def copy_template(current_dir):

    dest = pathlib.Path(sys.prefix) / TEMPLATE_DEST
    template_path = pathlib.Path(current_dir) / TEMPLATE_PATH

    if (dest / TEMPLATE_PATH).exists():
        return

    dest.mkdir(parents=True, exist_ok=True)

    shutil.copyfile(template_path, dest)

    print(f"Copied template {template_path} to {dest}")


def sanitize_filename(name: str) -> str:
    """Simplifies filename: lowercase, no whitespace, replaces special chars with underscores.

    Args:
        name: Original filename (without extension).

    Returns:
        Sanitized filename string.
    """
    # Lowercase
    name = name.lower()
    # Replace whitespace and underscores with hyphens
    name = re.sub(r"[\s_]+", "-", name)
    # Remove any non-alphanumeric characters (except underscores)
    name = re.sub(r"[^\w-]+", "", name)
    # Remove multiple hyphens
    name = re.sub(r"-+", "-", name)
    # Strip leading/trailing hyphens
    return name.strip("-")


def convert_notebooks(
    examples_dir: pathlib.Path, output_dir: pathlib.Path
) -> list[tuple[str, str]]:
    """Converts all notebooks in examples_dir to Markdown in output_dir.

    Args:
        examples_dir: Directory containing .ipynb files.
        output_dir: Directory where .md files will be saved.

    Returns:
        List of tuples (original_title, sanitized_filename).
    """
    notebooks = sorted(
        [p for p in examples_dir.glob("*.ipynb") if ".ipynb_checkpoints" not in str(p)]
    )
    converted_info = []

    if not notebooks:
        print(f"No notebooks found in {examples_dir}")
        return []

    print(f"Found {len(notebooks)} notebooks. Converting...")

    for nb_path in notebooks:
        original_title = nb_path.stem
        sanitized_name = sanitize_filename(original_title)
        output_filename = f"{sanitized_name}.md"

        print(f"  Converting '{original_title}' -> '{output_filename}'...")

        try:
            subprocess.run(
                [
                    "jupyter",
                    "nbconvert",
                    "--to",
                    "markdown",
                    "--output",
                    sanitized_name,
                    "--output-dir",
                    str(output_dir),
                    str(nb_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            converted_info.append((original_title, output_filename))

        except subprocess.CalledProcessError as e:
            print(f"Error converting {nb_path.name}:", file=sys.stderr)
            print(e.stderr, file=sys.stderr)

    return converted_info


def print_mkdocs_snippet(converted_info: list[tuple[str, str]]):
    """Prints the navigation snippet for mkdocs.yml.

    Args:
        converted_info: List of tuples (original_title, sanitized_filename).
    """
    if not converted_info:
        return

    print("\n" + "=" * 40)
    print("Add the following to your mkdocs.yml 'nav' section:")
    print("=" * 40)
    print("  - Examples:")
    for title, filename in converted_info:
        # Simple cleanup of title for the nav
        print(f"    - '{title}': 'examples/{filename}'")
    print("=" * 40 + "\n")


def main():
    """Main execution function."""

    current_dir = pathlib.Path(__file__).parent.resolve()

    # copy_template(current_dir)
    project_root = current_dir.parent

    examples_dir = current_dir
    docs_dir = project_root / "docs"
    output_dir = docs_dir / "examples"

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Convert notebooks to Markdown
    converted_info = convert_notebooks(examples_dir, output_dir)

    # 2. Print the mkdocs.yml snippet
    if converted_info:
        print_mkdocs_snippet(converted_info)
    else:
        print("No files were converted.")


if __name__ == "__main__":
    main()
