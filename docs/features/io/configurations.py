import sys

import tomli_w
import pytest

import poreflow as pf
import poreflow_dash as pfd

import pathlib




@pytest.fixture
def default_config():
    preload = {'input': {'folder_path': 'my_project/', 'file_name': 'my_measurement.fast5'}}
    return pfd.ConfigSchema(**preload).model_dump()

def test_default_schema(default_config):
    print(tomli_w.dumps(default_config, indent=2))

@pytest.fixture
def config():
    preload = {
        'input': {'folder_path': './', 'file_name': 'ont_measurement.fast5'},
        'env': {'verbose': 1, 'processes': 2},
        'event_filtering': {'max_ios': 300},
    }
    return pfd.ConfigSchema(**preload).model_dump()

@pytest.fixture
def config_file_on_disk(config):

    with open("poreflow.toml", "wb") as f:
        tomli_w.dump(config, f)


def test_config_raw(config_file_on_disk):
    # --8<-- [start:config_raw]
    import pathlib
    import tomllib

    with open("poreflow.toml", "rb") as f:
        config = tomllib.load(f) # (1)!

    input_config = config["input"] # (2)!

    file_name = input_config["file_name"]
    folder_path = pathlib.Path(input_config["folder_path"]) # (3)!
    print(f"Loading {file_name} from folder {folder_path}")

    with pf.File(folder_path / file_name) as f:
        raw = f.get_raw(channel=18)
        raw = raw.downsample(input_config["resample_to_freq"])

    # Further processing with raw
    # --8<-- [end:config_raw]


@pytest.fixture
def folder_path(config) -> pathlib.Path:
    return pathlib.Path(config["input"]["folder_path"])

@pytest.fixture
def file_name(config) -> str:
    return config["input"]["file_name"]

def test_config_event_detection(config, folder_path, file_name):
    # --8<-- [start:config_event_detection]
    event_config = config["event_finding"]
    env_config = config["env"]

    with pf.File(folder_path / file_name) as f:
        f.find_events(
            **event_config, # (1)!
            **env_config, # (2)!
        )
    # --8<-- [end:config_event_detection]


@pytest.fixture
def env_config(config) -> dict:
    return config["env"]

def test_config_event_selection(config, folder_path, file_name, env_config):

    event_config = config["event_finding"]

    with pf.File(folder_path / file_name) as f:
        f.find_events(
            **event_config,
            verbose=0,
            processes=2,
        )

    # --8<-- [start:config_event_selection]
    from poreflow.events import selection

    print("(1) Step finding:")
    with pf.File(folder_path / file_name) as f:
        f.find_steps(
            **config["step_finding"], # (1)!
            **env_config # (2)!
        )

        stats = selection.get_step_finding_stats(f) # (3)!

    print("\n(2) Event selection features:")
    print(stats.head())

    truth_table = selection.filter_from_config(stats, config["event_filtering"])

    print("\n(3) Event filtering results:")
    print(truth_table.head())

    mask = truth_table["all"]
    print(
        f"Selecting {sum(mask)} out of {len(mask)} "
        f"events ({sum(mask) / len(mask):.0%})"
    )
    with pf.File(folder_path / file_name) as f:
        f.filter_events(mask)
    # --8<-- [end:config_event_selection]




if __name__ == '__main__':
    sys.exit(pytest.main(['-qq']))
