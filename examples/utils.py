"""Utils for examples"""

import pathlib
import shutil
import tempfile
import glob

TMP_FOLDER_PREFIX = "tmp_"


def get_tmp_file(path: str):
    """Copies testing data to a temporary location"""

    path = pathlib.Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File {path} does not exist")

    tmp_dir = tempfile.mkdtemp(dir="./", prefix=TMP_FOLDER_PREFIX)

    shutil.copy(path, tmp_dir)

    return pathlib.Path(tmp_dir) / path.name


def remove_tmp_file():
    tmp_dirs = glob.glob(f"./{TMP_FOLDER_PREFIX}*")
    for tmp_dir in tmp_dirs:
        shutil.rmtree(tmp_dir)
