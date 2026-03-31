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

Downscaling is done using the `.downsample` method on poreFlow dataframe objects, like RawDataFrame or 
EventDataFrame.

### Example
```python linenums="1"
--8<-- "docs/features/filtering.py:block_1"
```

1. Get raw data for channel 0.
2. Downsample to 2.5 kHz

<div class="result" markdown>
```
--8<-- "docs/features/filtering.txt:block_1"
```
</div>


By default, only the current and voltage columns processed with an anti-aliasing filter before downsampling.

## Filtering

Unwanted high-frequency noise can be filtered using a 4th-order Bessel low-pass filter. 
Specify the cut-off frequency of the filter to from which frequency to attenuate the signal.

Downscaling is done using the `.apply_filter` method on poreFlow dataframe objects, like RawDataFrame or 
EventDataFrame.

### Example
```python linenums="1"
--8<-- "docs/features/filtering.py:block_2"
```

1. Filter with a filter with a cut-off frequency at 1000 Hz

<div class="result" markdown>
```
--8<-- "docs/features/filtering.txt:block_2"
```
</div>

By default, only the current and voltage columns are filtered. To change this behaviour, check out the 
reference.


??? warning "Do not confuse with `DataFrame.filter`"
    
    It is easy to confuse `pandas.DataFrame.filter` with `poreflow.BaseDataFrame.apply_filter`. 
    The former filters values in the columns or rows based on some argument, the later 
    does signal processing on the voltage/current columns of the DataFrame.


## Additional examples

Depending on your data, you might want to always first downsample to a specific frequency, and 
only then do further filtering or processing. This is often the case for high-frequency UTube data, 
which generally is first downsampled to around 5 kHz. An example of doing so:

```python linenums="1"
--8<-- "docs/features/filtering.py:block_3"
```
<div class="result" markdown>
```
--8<-- "docs/features/filtering.txt:block_3"
```
</div>

!!! info "DataFrame attributes"

    The example above demonstrates the three attributes in `poreflow.BaseDataFrame` used to keep track
    of filtering results.

    - `BaseDataFrame.sfreq_original` is set to the original sample rate of the file from which 
        the dataframe is read. It is not changed by filtering/downsampling.
    - `BaseDataFrame.sfreq` is the (downsampled) sample rate of the DataFrame.
    - `BaseDataFrame.filter_cutoff` is `None` if the event is unfiltered and set to the cut-off 
        frequency of the filter after filtering.


[decimate]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html
