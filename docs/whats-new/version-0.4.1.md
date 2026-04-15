# Version 0.4.1

Release date: April 15, 2026

This release introduces significant improvements to the poreFlow Dashboard, 
voltage plotting capabilities, and performance optimizations.

!!! warning

    This version depends on [`tsdownsample`][tsd], which does yet
    have a built version for Python 3.14. This means that 
    poreflow 0.4.1 only supports Python versions 3.11 to 3.13.
    
    If you are currently running Python 3.14, we  recommend installing 
    poreflow in a fresh virtual environment. Create the virtual environment 
    in your using: 

    ```shell
    uv venv --python 3.13
    ```

    For more information, check out the [Install][] page.

[tsd]: https://github.com/predict-idlab/tsdownsample
[Install]: ../getting-started/installation/#creating-a-virtual-environment

## Highlights

### Voltage Visualization
Added voltage plotting in channel views. To turn click :lucide-settings:,
to open the configuration, scroll to the voltage section, and turn on 
**Show voltage**.

### Simplified downsampling and filtering
Dashboard controls have been simplified. Downsampling happens 
under the hood in both the Channels and Events pages. 

The Channels page uses dynamic downsampling. The Events page uses 
the default downsample setting in the configuration ("Input" category)

These settings have also been removed from the
configuration file. Filtering can still be set in both pages. 

### Figure export
The figure in the Channels plot can be exported by clicking the 
:lucide-image-down: button. An annotation containing metadata is 
added automatically. Filename and metadata can also be manually 
specified.

### Plot axes controls
The user now has more control over the X and Y axis settings in
both the channel and voltage plots, click the :lucide-settings: 
button in both pages to learn more.

In the Events page, the user can select between an absolute timescale
(starting at the start time of the event) or a relative timescale
(starting at t=0 seconds).


## Changelog

### Dashboard & UI Improvements
- Added voltage plotting in channel views (#86)
- Improved IV curve visualization and export functionality
- Added voltage segments for detailed analysis
- Enhanced event duration filtering in detection
- Improved plot controls with better axis settings
- Added auto-scaling and downsampling controls
- Improved UI layout and button styles
- Enhanced error handling and user feedback
- Added display of processing statistics in plots
- Improved configuration validation
- Added option to hide whole config sections
- Fixed bug when saving config
- Improved dropdown menus in events plot
- Added better plot settings to events
- Simplified and hardcoded plot resolution
- Added starting time to default save filename
- Moved save PNG feature to bottom left
- Added title in figures
- New plot modal for better visualization

### Performance & Code Quality
- Optimized downsampling in backend by default
- Improved filtering performance
- Enhanced multiprocessing support
- Better memory management
- Cleaned up UI components
- Removed redundant stores
- Fixed x-axis update shifting issues
- Added spacing between voltage-current plots
- Set frequencies to integers in schema
- Improved list view performance
- Enhanced voltage configuration
- Better handling of integer columns in downsampling
- Improved exception handling for event detection
- Cleaned up and refactored tests
- Improved logging

### Bug Fixes
- Fixed bug where x-axis update shifts x-axis position
- Fixed event overlay subplot target
- Fixed dropdown menu in events plot
- Fixed DNA prediction plot
- Fixed bug when saving config
- Fixed hiding when excluded=True in form creation
- Fixed boundary trimming in event detection
- Fixed configuration error handling
- Fixed issues with channel numbering
- Fixed downsampling issues with integer columns
- Fixed file locking on Windows
- Fixed voltage view display
- Fixed list view performance issues

### New Features
- Added voltage plot in channel view (#86)
- Added IV curve visualization improvements
- Added voltage config options
- Added relative/absolute limit settings
- Added better plot settings to events
- Added option to hide whole config sections
- Added display of raw sampling rate and processing frequencies
- Added effective sampling rate indicator
- Added channel filter cutoff functionality
- Added resampler dependency for better plot handling
- Added back PNG save feature
- Added star include for categories
- Added button handler for boolean schema fields
- Added filter cutoff to text box
- Adjusted default textbox to include sampling rate

### Documentation
- Updated notebooks with new features
- Improved IV curve notebook
- Updated ONT processing notebook
- Added better examples and documentation
- Improved notebook examples

### Code Refactoring
- Refactored voltage plotting code
- Improved event detection algorithms
- Enhanced step detection performance
- Cleaned up and optimized codebase
- Removed redundant code
- Improved type hints and documentation

## Authors
Thijn Hoekstra and Xiuqi Chen, see [Authors].

[Authors]: ./../authors