import sys

import tomli_w
import pytest

import poreflow as pf
import poreflow_dash as pfd





def test_default_schema():
    preload = {'input' : {'folder_path': 'my_project/', 'file_name': 'my_measurement.fast5'}}
    config = pfd.ConfigSchema(**preload).model_dump()
    print(tomli_w.dumps(config, indent=2))

if __name__ == '__main__':
    sys.exit(pytest.main(['-qq']))
