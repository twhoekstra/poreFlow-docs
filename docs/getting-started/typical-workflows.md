

## I-V curve analysis

An example [Jupyter notebook](https://gitlab.tudelft.nl/xiuqichen/poreFlow/-/blob/main/notebooks/IV_curve.ipynb?ref_type=heads) is provided for processing I-V curve measurements of a nanopore.

Once the poreFlow Python environment is configured, download this notebook and load your data file (.dat) to begin processing.

## Sequencing analysis

For processing sequencing data files (.fast5 or .dat), an example [Jupyter notebook](https://gitlab.tudelft.nl/xiuqichen/poreFlow/-/blob/main/notebooks/ONT_processing.ipynb?ref_type=heads) is available.

<!-- more details and usage options need to be provided here. Comments are included in HTML -->

A single [config file](https://gitlab.tudelft.nl/xiuqichen/poreFlow/-/blob/main/notebooks/parameters.toml?ref_type=heads) centralizes all measurement parameters, including the file name, event-finding settings, and filtering criteria.

<br>
<br>
<br>
<br>
<br>
<br>
<br>


## A typical nanopore sequencing workflow

```mermaid
graph LR
    A[Measurement] -->|Preprocessing| B[Refined measurement]
    B -->|Event finding| C[Events]
```

## poreFlow

```mermaid
graph TD;
    A@{ shape: cyl, label: "ONT File<br><tt>.fast5</tt>"}<-->|Read/write|D[File<br><tt>poreflow.File</tt>]
    C@{ shape: cyl, label: "UTube File<br><tt>.dat</tt>"}-->|Converted|A
    D-->|Read a channel|B[Measurement<br><tt>poreflow.RawDataFrame</tt>]
    D<-->|"Find events<br><tt>.find_events()</tt>"|E[Events<br><tt>poreflow.EventsDataFrame</tt>]
%%    E-->|Saved|D
%%    D-->|"Get events<br><tt>.get_events()</tt>"|Ex
    D<-->|"Find steps in events<br><tt>.find_steps()</tt>"|G[Steps<br><tt>poreflow.StepsDataFrame</tt>]
%%    G-->|Saved|D
    E-->F[Events with stats<br><tt>poreflow.EventsDataFrame</tt>]
    G-->F
    F-->|Filter using stats|H["Boolean Mask<br><tt>pandas.Series</tt>"]
    H-->|"Filter events<br><tt>.filter_events()</tt>"|D
    D-->|"Get event<br><tt>.get_event()</tt>"|I[Steps<br><tt>poreflow.EventDataFrame</tt>]
```



