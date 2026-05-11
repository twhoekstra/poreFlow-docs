# Configurations

When doing large-scale analysis, you might want to collect all your processing settings (e.g. those for 
event-finding, plotting, step detection) into one file. 

PoreFlow supports a [TOML][] file used to store and maintain parameters. This document explains [when](#when-to-use-configurations) and how to use 
configurations, provides [usage examples](#code-examples), and details [all available settings](#configuration-reference).

## When to use configurations

It is recommended to use configurations when your use case has or requires:

- **Reproducible analyses**: You need to document and reproduce exact parameter values across multiple runs or share analyses with colleagues
- **Batch processing**: Running the same analysis on multiple files with consistent parameters
- **Parameter tuning**: Experimenting with different parameter combinations and need to track which settings produced which results
- **Team collaboration**: Multiple people need to use the same analysis parameters


!!! tip "When not to use configurations"

    Consider not using  configurations when your use case has or requires:

    - **One-off analyses**: Simple, exploratory (initial) analyses where you're testing a single file with default parameters
    - **Quick scripts**: Short scripts with few parameters
    - **Highly dynamic parameters**: When parameters need to be computed at runtime based on input data characteristics

## Configurations in scripts versus poreFlow dashboard

The poreFlow Python module and dashboard have different use-cases, and thus treat configurations a little differently. 
Their approach to configurations is summarized below:



<div class="grid cards" markdown>

-   :material-language-python:{ .lg .middle } __Python Module__

    ---
    
     The Python module is intended as building blocks for your own analysis. This means:

    - Your code reads the configuration file.
    - Your code decides which functions use which parts of the configuration file.
    
    While a lot more flexible, consider that requires some more set-up on your end. Note that poreFlow has been 
    designed around this use case, which makes things easier. For usage examples, check out:

    [:octicons-arrow-right-24: Code examples](#code-examples)

    !!! note 
        As mentioned in the previous section, consider forgoing configurations for one-offs and quick analysis.

[//]: # (    [:octicons-arrow-right-24: When to use configurations]&#40;#when-to-use-configurations&#41;)

</div>

<div class="grid cards" markdown>

-    :lucide-monitor:{ .lg .middle } __Dashboard__

    ---
    
    The dashboard uses configurations throughout:
        - Settings indide the dashboard can be stored to a configuration file
        - A configuration file can be loaded to use saved settings in a new session.
    
      To learn more, check out the Dashboard features pages:
        
      [:octicons-arrow-right-24: Dashboard features](../dashboard)

</div>

## TOML Language

Configuration files use [TOML (Tom's Obvious, Minimal Language)][TOML], a configuration file format that is. 
Advantages of TOML are:

- **Human-readable**: Clear syntax with sections (tables) and key-value pairs
- **Types**: Supports strings, integers, floats, booleans, arrays, and nested structures
- **Widely supported**: In Python via the [`tomllib`][tomllib] module (or `tomli` for older versions))

A snippet of a configuration in the TOML language containing event finding parameters:

```toml title="poreflow.toml"
--8<-- "docs/features/io/configurations.txt:31:48"
```

??? note "Spacing and lists in TOML files"
    
    Note some parameters like `open_state_range` are a list. TOML files have quite flexible formatting, 
    in this example these lists have written over multiple lines:
    
    ```toml
    open_state_range = [
      200,
      300,
    ]
    ```

    A more brief notation is also possible:

    ```toml
    open_state_range = [200, 300]
    ```

    Use whatever you prefer.




## Full example

Shown below is an example of a TOML file with all possible parameters. The next section describes the meaning and 
usages of each parameter.

```toml title="poreflow.toml"
--8<-- "docs/features/io/configurations.txt:default_schema"
```


## Configuration Reference

This section documents all available configuration settings, organized by section. Each setting corresponds to parameters used in PoreFlow's analysis functions.

### Input settings
> Section name: `[input]`

Parameters controlling file input and initial signal processing.


| <div style="min-width:150px">Setting</div> | Type | Default     | Description                                                                                                                                          |
|--------------------------------------------|------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`                                     | str  | "My File"   | Display name of the file for identification in outputs and logs                                                                                      |
| `folder_path`                              | str  | *required*  | Path to the folder containing the data file                                                                                                          |
| `file_name`                                | str  | *required*  | Name of the data file to process (e.g., `260309_XC_H3-C2_pore1_perf1_f2.dat`)                                                                        |
| `resample_to_freq`                         | int  | 5000        | Target sample rate (Hz) for downsampling the signal before processing. Lower values reduce data size and processing time but may lose fine details   |

### Output settings

> Section name: [output]

Parameters controlling output locations.

| <div style="min-width:150px">Setting</div> | Type | Default | Description                                                                    |
|--------------------------------------------|------|---------|--------------------------------------------------------------------------------|
| `path`                                     | str  |  "./"   |  Path to the directory where output files (annotations, figures) will be saved |

### Environment settings

> Section name: [env]

Environment and runtime parameters.

| <div style="min-width:150px">Setting</div> | Type | Default | Description                                                                                                                             |
|--------------------------------------------|------|---------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `processes`                                | int  | 2       | Number of parallel processes to use for multi-channel processing. Higher values use more CPU cores but may have diminishing returns[^1] |
| `verbose`                                  | int  |  0      | Verbosity level. 0 = silent, higher values produce more detailed output                                                                 |

[^1]: Note that `processes` must be equal to or smaller than the number of processes available on your device. 
    To find out the number of cores available on your PC, consult [these intructions][cores PC]. For Mac, 
    open a terminal and run `sysctl -n hw.ncpu`. 

### Plot settings

> Section name: [plot]

Parameters controlling figure output.

| <div style="min-width:150px">Setting</div> | Type | Default      | Description                                        |
|--------------------------------------------|------|--------------|----------------------------------------------------|
| `out`                                      | str  |  "./Figures" |  Path to the directory where figures will be saved |

### Event detection setting

> Section name: [event_finding]

Parameters for detecting events in the recording.

| <div style="min-width:150px">Setting</div> | Type       | Default    | Description                                                                                                                                                                                                       |
|--------------------------------------------|------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `open_state_range`                         | list[int]  | [200, 300] | Current range in pA that defines the open state (open pore). Values outside this range are considered potential events                                                                                            |
| `voltage_range`                            | list[int]  | [175, 185] | Acceptable voltage range in mV. Data outside this range is excluded from analysis                                                                                                                                 |
| `closing_iterations`                       | int        | 10         | Number of morphological closing operations applied to the event mask. Higher numbers allow for longer gaps in an event that have an incorrect voltage or an open state current.                                   |
| `boundary_trim`                            | list[int]  | [1, 1]     | Time in milliseconds to trim from the start and end of each detected event. Negative values can be used to expand an event to include samples before and after the detected event. Format: [start_trim, end_trim] |
| `n_components`                             | int        | 3          | Number of components for the Gaussian Mixture Model (GMM) used to fit the open state current distribution                                                                                                         |
| `degree`                                   | int        | 2          | Degree of the polynomial fit applied to the open state current                                                                                                                                                    |
| `min_frac_os`                              | float      | 0.01       | Minimum fraction of the recording that must be in the open state. Defaults to 1%. If less than this fraction is open state, the channel is rejected.[^2]                                                          |
| `min_duration`                             | float      | 1.0        | Minimum duration in seconds for a detected event. Events shorter than this are filtered out immediately after detection                                                                                           |

[^2]: Mainly important for ONT devices. ONT devices contain many channels for which each is analysed for events. 
    Some channels are blocked for the full duration of the recording, thus containing few samples within `open_state_range`.
    Channels with a low fraction of samples at open state current are bad and event detection is stopped early. Note 
    that this is also useful for UTube measurements, as this will throw an error if the user selects a wrong open 
    state range. If there are an insane amount of reads (i.e. very little time at open state), you can consider setting 
    this to 0.1% or lower.

### Step finding settings

> Section name: [step_finding]

Parameters for detecting steps within events. 

| <div style="min-width:150px">Setting</div> | Type    | Default | Description                                                                                                    |
|--------------------------------------------|---------|---------|----------------------------------------------------------------------------------------------------------------|
| `sensitivity`                              | float   | 3.0     | Sensitivity of the step finder algorithm. Higher values result in fewer, more significant steps being detected |
| `min_level_length`                         | int     | 10      | Minimum number of samples for a step to be valid. Prevents detection of very short, noise-like steps           |

### Event selection settings

> Section name: [event_filtering]

Parameters for filtering events based on their characteristics after step finding.

| <div style="min-width:150px">Setting</div> | Type     | Default | Description                                                                                                                                |
|--------------------------------------------|----------|---------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `min_duration`                             | float    | 1.0     | Minimum duration in seconds for an event to pass filtering                                                                                 |
| `min_n_steps`                              | int      | 45      | Minimum number of steps required in an event                                                                                               |
| `max_n_steps`                              | int      | 800     | Maximum number of steps allowed in an event                                                                                                |
| `min_binned_entropy_of_means`              | float    | 2.5     | Minimum binned entropy of step means. Typical value of 2.5 for M2 MspA DNA sequencing. Measures the variability/disorder of current levels |
| `min_step_rate`                            | float    | 12.0    | Minimum step rate in Hz. Typical value of 12 Hz for Hel308 at 37°C with 1 mM ATP                                                           |
| `min_ios`                                  | float    | 0.0     | Minimum local open state current in pA. Events with open state below this are rejected                                                     |
| `max_ios`                                  | float    | 300.0   | Maximum local open state current in pA. Events with open state above this are rejected                                                     |

### DNA-peptide boundary detection settings

> Section name: [boundary]

!!! warning "Work in progress"
    These settings are currently WIP in poreFlow. Using these is not recommended yet. Note that their names might 
    also change in future poreflow versions.

Parameters for DNA-peptide boundary detection and alignment.

| <div style="min-width:150px">Setting</div> | Type | Default         | Description                                                                  |
|--------------------------------------------|------|-----------------|------------------------------------------------------------------------------|
| `template_DNA_5_3`                         | str  | TCCT...CGCT[^3] |  Template DNA sequence (5' to 3') used for boundary detection and alignment  |
| `trim_right`                               | int  | 8               | Number of bases to trim from the right end of events during alignment        |
| `ref_length`                               | int  | 54              | Reference length in bases for the expected DNA sequence                      |
| `segment_step_to_end`                      | int  | 4               | Number of steps from the end of the event to consider for boundary detection |
| `window_length`                            | int  | 40              | Window length in bases for boundary analysis                                 |

[^3]: Middle nucleotides have been removed here for brevity. Full sequence: `TCCTTTTATCGTCATCATCTTTGTAATCGCCGCT`

## Code examples

These examples below use the default config file, with one alteration: the [environment](#environment-settings) 
setting `verbose` is set to 1.

### Loading a raw recording

This example shows how stored filenames and folder can be used to parametrize from where to load a file.

```python linenums="1"
--8<-- "docs/features/io/configurations.py:config_raw"
```

1. Load a config file using [`tomllib`][tomllib].
2. Read the input section of the file

<div class="result" markdown>
```text
--8<-- "docs/features/io/configurations.txt:config_raw"
```
</div>

### Event detection

This example shows how a configuration file can be used for setting arguments for event finding. 
Note that it can be cleanly and easily implemented using argument [unpacking]. See the inline comments 
(the :lucide-circle-plus: icons) in the code below for more information.

```python linenums="1"
--8<-- "docs/features/io/configurations.py:config_event_detection"
```

1. [`poreflow.File.find_events`][] is an interface for [`poreflow.events.detection.find_events`][]. <br><br>If the TOML file
    has an `event_finding` section with the same keys as [`poreflow.events.detection.find_events`][] 
    (`open_state_range`, `min_duration`, etc.), it is easiest and cleanest to simply [unpack][unpacking] the arguments 
    into the method using the `**` syntax.
2. We can also unpack the environment section into this method, as [`poreflow.File.find_events`][] takes both a 
    `verbose` and `processes` keyword argument.

<div class="result" markdown>
```text
--8<-- "docs/features/io/configurations.txt:config_event_detection"
```
</div>


### Step finding and event selection

This example show how stored filenames and folder can be used to parametrize from where to load a file.

```python linenums="1"
--8<-- "docs/features/io/configurations.py:config_event_selection"
```

1. Like what was shown in the previous example, [`poreflow.File.find_steps`][] is an interface for [`poreflow.EventDataFrame.find_steps`][]. <br><br>If the TOML file
    has an `step_finding` section with the same keys as [`poreflow.EventDataFrame.find_steps`][] 
    (`sensitivity` and `min_level_length`), it is easiest and cleanest to simply [unpack][unpacking] the arguments 
    into the method using the `**` syntax.
2. We can also unpack the environment section into this method, as [`poreflow.File.find_steps`][] takes both a 
    `verbose` and `processes` keyword argument.

<div class="result" markdown>
```text
--8<-- "docs/features/io/configurations.txt:config_event_selection"
```
</div>

[TOML]: https://toml.io/
[tomllib]: https://docs.python.org/3/library/tomllib.html
[cores PC]: https://www.intel.com/content/www/us/en/support/articles/000029254/processors.html
[unpacking]: https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
