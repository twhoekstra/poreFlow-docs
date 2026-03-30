import poreflow as pf

import pytest

def test_block_1():
    # --8<-- [start:block_1]
    with pf.File("utube_measurement.dat") as f:
        raw = f.get_raw()  # (1)!
        print(f"File sample rate {f.sfreq} Hz")

    raw = raw.downsample(2500) # (2)!

    print(f"Original sample rate {raw.sfreq_original} downsampled to {raw.sfreq} Hz")
    # --8<-- [end:block_1]

def test_block_2():
    # --8<-- [start:block_2]
    with pf.File("utube_measurement.dat") as f:
        raw = f.get_raw()  # (1)!
        print(f"File sample rate {f.sfreq} Hz")

    raw = raw.downsample(2500) # (2)!

    print(f"Original sample rate {raw.sfreq_original} downsampled to {raw.sfreq} Hz")
    # --8<-- [end:block_2]