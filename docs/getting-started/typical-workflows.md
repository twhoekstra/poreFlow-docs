

## I-V curve analysis

An example [Jupyter notebook file](https://gitlab.tudelft.nl/xiuqichen/poreFlow/-/blob/main/notebooks/IV_curve.ipynb?ref_type=heads) is provided for processing I-V curve measurement of a nanopore.

Once the poreFlow python env is configured properly, download this ipynb file to load the data file (.dat) for processing. 

## Sequencing analysis

For processing sequencing measurement data files (.fast5 or .dat), an example [Jupyter notebook file](https://gitlab.tudelft.nl/xiuqichen/poreFlow/-/blob/main/notebooks/ONT_processing.ipynb?ref_type=heads) is developed.

<!-- more details and usage options need to be provided here. Comments are included in HTML -->

A single [config file](https://gitlab.tudelft.nl/xiuqichen/poreFlow/-/blob/main/notebooks/parameters.toml?ref_type=heads) is used to aggregate all parameters related to the measurement, such as file name, event finding parameters, and filtering parameters.

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



