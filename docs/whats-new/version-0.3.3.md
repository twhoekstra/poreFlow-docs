# Version 0.3.3

Release date: March 1, 2026

## Highlights
This release includes CI/CD pipeline enhancements, bug fixes, and new utility functions. Release is intended 
to finalize publishing and CI/CD design choices for a while. There are no major functionality 
changes since 0.2.5 and is fully cross-compatible with this version.

## Changelog
- **Bessel filter utility** - Added `bessel_filter` function to `src/poreflow/utils.py` for signal processing
- **GitLab CI enhancements** - Updated `.gitlab-ci.yml` with better publishing tests and managed Python support
- **Versioning from git tags** - Added dynamic versioning system that reads from git tags
- **Build system improvements** - Force use of managed Python during builds for consistency
- **Caching updates** - Improved dependency caching for faster CI/CD pipelines
- **Publish job change** - Updated publish job to only publish source distributions. Wheel distributions should
    be built manually on Windows/Mac devices. The

## Authors
Thijn Hoekstra and Xiuqi Chen, see [Authors].

[Authors]: ./../authors