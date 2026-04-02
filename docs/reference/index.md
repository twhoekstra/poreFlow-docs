# Python API Reference

This is the reference for the classes and functions in the poreFlow module.

## Most used classes

| Class                                     | Description                                              |
|:------------------------------------------|:---------------------------------------------------------|
| [poreflow.File][]                         | input/output to `.fast5` and `.dat` files.               |
| [poreflow.RawDataFrame][]                 | Table for storing full measurements on a single channel  |
| [poreflow.EventsDataFrame][]              | Table for storing events and their properties            |
| [poreflow.EventDataFrame][]               | Table for storing an event and its current data          |
| [poreflow.StepsDataFrame][]               | Table for storing steps for one or more events           |


## Events

Submodules and classes related to events.

| Class                             | Description                                                                                |
|:----------------------------------|:-------------------------------------------------------------------------------------------|
| [poreflow.EventsDataFrame][]      | Table for storing events and their properties                                              |
| [poreflow.EventDataFrame][]       | Table for storing an event and its current data                                            |
| [poreflow.events.detection][]     | Submodule for detecting events in measurements                                             |
| [poreflow.events.open_state][]    | Submodule for detecting an open state in a measurement                                     |
| [poreflow.events.voltage_state][] | Submodule for detecting whether the voltage is in range during a measurement               |
| [poreflow.steps.metrics][]        | Metrics used to describe an event based on step information                                | 
| [poreflow.events.selection][]     | Submodule for describing events using features and selecting good events by these features |

## Steps

Submodules and classes related to steps.

| Class                          | Description                                                              |
|:-------------------------------|:-------------------------------------------------------------------------|
| [poreflow.StepsDataFrame][]    | Table for storing steps for a single or many events                      |
| [poreflow.steps.changepoint][] | Information-theory based change point detection algorithm written in C++ |
| [poreflow.steps.cpic][]        | Change Point Information Criterion calculation functions                 |
| [poreflow.steps.metrics][]     | Metrics used to describe an event based on step information              |
| [poreflow.steps.predict][]     | Submodule to predict a step sequence from a DNA nucleotide sequence      |
| [poreflow.steps.sequence][]    | (Work in progress) Hidden Markov Model's for sequencing/variant calling  |

## General

General tools

| Class                       | Description                        |
|:----------------------------|:-----------------------------------|
| [poreflow.constants][]      | Constants used throughout poreFlow |
| [poreflow.utils][]          | General utility functions          |

## Visualisation

Plotting tools

| Class              | Description               |
|:-------------------|:--------------------------|
| [poreflow.plots][] | Plotting helper functions |

## Parallel processing

Plotting tools

| Class                 | Description                                |
|:----------------------|:-------------------------------------------|
| [poreflow.parallel][] | Tools for monitoring multiprocessing tasks |
