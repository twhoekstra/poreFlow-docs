import sys

import poreflow as pf

import pytest

def test_block_1():
    # --8<-- [start:block_1]
    with pf.File("utube_measurement.dat") as f:
        raw = f.get_raw()  # (1)!
        print(f"File sample rate {f.sfreq} Hz, {len(f)} samples.")

    raw = raw.downsample(2500) # (2)!

    print(f"Original sample rate {raw.sfreq_original} downsampled to {raw.sfreq} Hz, now {len(raw)} samples.")
    # --8<-- [end:block_1]

def test_block_2():
    # --8<-- [start:block_2]
    with pf.File("utube_measurement.dat") as f:
        raw = f.get_raw()

    raw = raw.apply_filter(1000) # (1)!

    print(f"Sample rate {raw.sfreq} filtered with a cutoff at to {raw.filter_cutoff}.")
    # --8<-- [end:block_2]

def test_block_3():
    # --8<-- [start:block_3]
    with pf.File("utube_measurement.dat") as f:
        raw = f.get_raw()

    raw = raw.downsample(5000).apply_filter(1000)

    print(f"Original sample rate: {raw.sfreq_original} Hz")
    print(f"Downsampled to:       {raw.sfreq} Hz, ")
    print(f"Filtered to:          {raw.filter_cutoff} Hz, ")
    # --8<-- [end:block_3]


if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"]))
