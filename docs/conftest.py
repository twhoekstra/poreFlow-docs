import shutil
import sys
from pathlib import Path
from importlib import resources as impresources

import pytest

assets = Path(__file__).parents[1] / "assets"

DAT_FILE = assets / "utube_measurement.dat"
FAST5_FILE = assets / "ont_measurement.fast5"


@pytest.fixture(autouse=True)
def test_wrapper(request):
    # Setup: This runs BEFORE the test
    name = request.node.name.replace("test_", "")
    print(f"\n--8<-- [start:{name}]")

    yield

    # Teardown: This runs AFTER the test
    print(f"--8<-- [end:{name}]\n")

@pytest.fixture(autouse=True)
def tmp_dir_loaded(monkeypatch, tmp_path):

    # Copy the file into the temp directory
    shutil.copy(DAT_FILE, tmp_path / DAT_FILE.name)
    shutil.copy(FAST5_FILE, tmp_path / FAST5_FILE.name)

    # Change the working directory for this test
    monkeypatch.chdir(tmp_path)

    return tmp_path

