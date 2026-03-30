# Version 0.4.0

Release date: March 9, 2026

This release introduces major architectural changes to improve performance, flexibility, and usability. 
Key changes include the introduction of "Annotation" files and an upgraded dashboard. 

## Highlights

### Annotations 

!!! info

    For a complete description of the annotations system, check out: [Annotations][].

Analysis results like events and steps are now stored in a separate file from raw data, allowing for more flexible 
data management and easier sharing of analysis results without raw data. Consider this example project:

```title="Project structure"
my-project/
 └── measurement.dat 
```

Then this `.dat` data file, can be opened using [`poreflow.File`][F]:

```python linenums="1"
import poreflow as pf

with pf.File("measurement.dat") as f: # (1)!
    f.find_events() # (2)!
```

Processing results are stored in a separate file with the `annot.fast5` extension.

```title="Project structure (after opening)"
my-project/
 ├── measurement.dat    
 ├── measurement.fast5    
 └── measurement.annot.fast5  <-- Analysis results (read-write)
```

This new system is fully backwards compatible with poreFlow 0.3.X, as annotation opening is managed under the 
hood by [`poreflow.File`][F]. As a result, no changes in processing scripts are needed. Note that the annotations 
system has many advantages for most users, to learn more, check out the 
[Annotations][] feature page.

### Parallel Processing
Enhanced parallel processing capabilities for event and step detection, with improved efficiency and better handling of multiprocessing across different platforms.

### Dashboard Improvements
The dashboard has seen major improvements in settings management, UI refinements, and better handling of configuration files. New features include auto-scaling, better downsampling controls, and improved error handling.

## Migration Guide

No migration needed! The system automatically:

1. Creates annotation files when opening existing data files
2. Maintains backward compatibility with existing code
3. Handles both `.fast5` and `.dat` files seamlessly

## Changelog

### Architecture & Core Changes
- Separated annotations into their own file for better data management
- Refactored `File` class into `DataFile` (raw data) and `File` (with annotations)
- Improved parallel processing for event and step detection
- Added pointer system for efficient data access in `DataFile`
- Enhanced downsampling and filtering API
- Added support for alternative annotation paths

### Dashboard & UI Improvements
- Refactored settings system with TOML configuration
- Added auto-scaling and better downsampling controls
- Improved UI for channel and event viewers
- Enhanced error handling and user feedback
- Added validation for configuration settings
- Improved layout and button styles
- Added display of raw sampling rate and processing frequencies

### Performance & Code Quality
- Optimized multiprocessing for different platforms (Windows/Linux)
- Improved file locking and I/O handling
- Enhanced downsampling with better handling of integer columns
- Added better exception handling for event detection
- Cleaned up and refactored tests for CI/CD
- Improved logging and removed redundant print statements

### Bug Fixes
- Fixed bug in event detection with `start_idx` handling
- Fixed issues with channel numbering in open state fit datasets
- Resolved problems with file locking on Windows
- Fixed downsampling issues with integer columns
- Corrected boundary trimming in event detection
- Fixed configuration error handling in dashboard

### New Features
- Added IV curve visualization and export functionality
- Implemented voltage segments for analysis
- Added support for manual IV curve processing
- Enhanced event duration filtering in detection
- Added display of processing statistics in plots
- Improved handling of unavailable data in `poreflow.File`

### Documentation
- Updated AGENTS.md with new features and usage information
- Added deprecation notices for older functionality
- Improved notebook examples

## Authors
Thijn Hoekstra and Xiuqi Chen, see [Authors].

[Annotations]: ../features/io/annotations.md
[Authors]: ./../authors
[F]: ../../reference/poreflow/#poreflow.File