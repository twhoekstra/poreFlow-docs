
Overall requirements:

- Complete analysis pipeline in Python, rather than partially/fully in MATLAB
- Support for a free translocation workflow

Features to be implemented based on meeting, by processing step. Particular stakeholders are mentioned.

## Input/Output
Tools for saving and reading sequencing files.

- Extremely fast I/O :lucide-check:

## Preview tools
Methods for viewing measurement sessions for initial quality control.

- ONT: Preliminary reports of channels, such as number of channels with good reads in the flow cell, along with duration of measurements
- ONT: Information from multiplexer scans
- ONT: Overview showing of measurements across all channels
- Measurement information
- ONT: Show flow-cell ID


## Event detection/selection
Tools for detecting events/reads in measurements, in addition to filtering them by properties or by hand.

- Event detection for short and plentiful events in free translocation (Tor, Luning)
- GUI where even properties, e.g. dwell time or current drop/blockade are shown. Points in this plot can be selected can be selected, e.g. with a lasso to view/select a group of events and optionally create a consensus sequence.

## Step finding
Tools to segment steps in events.

- Step finding in short events (Tor)
- Step finding for irregular steps (Tor)

## Viewing and annotating events
Tools that allow for annotating (sections of) events.

- Plotting power spectrum of a manually selected region in a raw trace (Luning)
- Add a digital filter (4th-order Bessel filter) low-pass filter.
- Allow for cleaning up and event by cutting parts, e.g. removing parts where the voltage is flipped/the pore is gating (Luning)
- Option to assign a quality score to an event
- Filtering events based on a certain pattern. Search for events that match a DNA/peptide sequence (Justas)
- Manual inspection of events
- Automatic selection of good events based on parameters for helicase sequencing/free translocation
- Fast event loading, possibly by downsampling (Justas) :lucide-check:
- Splitting events/modifying the end of it, e.g for when two events follow each other rapidly and are segmented as one event
- User-friendly method to segment and annotate multiple regions in events, i.e. DNA-peptide-reread-reread2.
- Good live zoom feature.

## Alignment/consensus generation

Methods for aligning two or more sequences including the creation of consensus sequences.

- [] Alignment/consensus sequence generation
- [] Tool to overlay two consensus sequences for comparison
- [] Consensus generation for irregular steps (Tor)

## Variant calling
Tools that allow for classification of events.

- Variant calling module in Python


Potential resources
-------------------
- Ritmejeris, J., et al. (2025). "Terminal conjugation enables nanopore sequencing of peptides." bioRxiv: 2025.2011. 2012.687956.
- Rukes, V., et al. (2025). "Charge-based fingerprinting of unlabeled full-length proteins using an aerolysin nanopore." bioRxiv: 2025.2001. 2013.632743.
- Martin, A., et al. (2025). "Identification of Capture Phases in Nanopore Protein Sequencing Data Using a Deep Learning Model." arXiv preprint arXiv:2511.01277.
- Plesa, C. and C. Dekker (2015). "Data analysis methods for solid-state nanopores." Nanotechnology 26(8): 084003.
- Existing software from ONT/Elements/Axon instruments/Clampfit








