# Filtering and Downsampling

## Overview

PoreFlow, features tools to both filter and downsample raw nanopore sequencing data. 
These methods are described on this page.

## Key Concepts

<div class="grid cards" markdown>

-   :lucide-waves-arrow-down:{ .lg .middle } __Downsampling__

    ---

    Reduces the number of samples in a dataset. 

    Used for:

    - Faster visualization
    - Efficient storage
    - Reducing computational load

-   :lucide-sliders-horizontal:{ .lg .middle } __Filtering__

    ---

    Retains the same number of samples but removes unwanted frequencies. 
    
    Used for:

    - Noise reduction
    - Removing artifacts


</div>

## Downsampling

Downsampling reduces the sampling frequency by an integer factor. It is particularly useful for 
UTube data, which can be recorded at high sample rates (50 kHz), which for long measurements leads to 
a large dataset. Downsampling to, say, 5 kHz plotting is a great way to improve performance.

Under the hood, [`scipy.signal.decimate`][decimate] is used to downsample the signal, which applies an 
anti-aliasing filter before downsampling.


### Example
```python linenums="1"
import poreflow as pf

with pf.File("my_measurement.dat") as f:
    raw = f.get_raw()  # (1)!
    print(f"File sample rate {f.sfreq}")


raw = raw.downsample(2500) # (2)!

print(f"Original sample rate {raw.sfreq_original} downsampled to {raw.sfreq}")
```
<div class="result" markdown>
```
import tensorflow as tf
```
</div>
1. Get raw data for channel 0.
2. Downsample to 2.5 kHz





By default, only the current and voltage columns are filtered using a 4th-order Bessel filter.
### Filtering


## Methods

### `BaseDataFrame.apply_filter`

Applies a filter to the specified columns of the DataFrame.

**Parameters:**
- `cutoff` (float): The cutoff frequency for the filter in Hz.
- `cols` (list, optional): Columns to filter. Defaults to `[pf.VOLTAGE_COL, pf.CURRENT_COL]`.
- `method` (str, optional): Filtering method. Options are `"bessel4"` (default) or `"decimate"`.
- `verbose` (int, optional): Verbosity level (0, 1, or 2).

**Returns:**
- `BaseDataFrame`: A new DataFrame with the filtered data.

**Behavior:**
- If `method="decimate"`, the DataFrame is downsampled by truncating other columns to match the filtered data length.
- If `method="bessel4"`, the DataFrame retains the same number of samples, and the `filter_cutoff` attribute is updated.

### `BaseDataFrame.downsample`

Downsamples the DataFrame to a specified sampling frequency.

**Parameters:**
- `to` (float): Target sampling frequency in Hz. If `None` or greater than the current sampling frequency, returns the original DataFrame.
- `cols` (list, optional): Columns to downsample. Defaults to `None`, which uses the default columns for filtering.

**Returns:**
- `BaseDataFrame`: A new DataFrame with the downsampled data.

**Behavior:**
- Uses `apply_filter` with `method="decimate"` internally.
- Updates the `start_idx` attribute to reflect the new sampling frequency.

## Examples

### Downsampling with `RawDataFrame`



### Filtering with `EventsDataFrame`

```python
import poreflow as pf

# Load events data
events_data = pf.EventsDataFrame.load("path/to/events_data.h5")

# Apply a low-pass filter with a cutoff frequency of 1 kHz
filtered_data = events_data.apply_filter(cutoff=1000, method="bessel4")

# Plot the filtered data
filtered_data.plot(y="i", x="abs")
```

## Notes

- **Default Columns**: By default, only the current (`pf.CURRENT_COL`) and voltage (`pf.VOLTAGE_COL`) columns are filtered or downsampled. Other columns are either truncated (for downsampling) or left unchanged (for filtering).
- **Sampling Frequency**: The `sfreq` attribute is updated to reflect the new sampling frequency after downsampling.
- **Filter Cutoff**: The `filter_cutoff` attribute is updated to reflect the cutoff frequency used in filtering.

## References

- [poreFlow Documentation](https://poreflow.readthedocs.io/)
- [poreFlow GitHub Repository](https://github.com/poreflow/poreflow)
- [scipy.signal.bessel](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.bessel.html)
- [scipy.signal.filtfilt](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html)
- 


[decimate]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html
