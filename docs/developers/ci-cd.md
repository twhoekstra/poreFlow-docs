# CI/CD

poreFlow uses Continuous Integration/Continuous Deployment (CI/CD) to automate 
package testing, building, and packaging.

## Windows runner:

### Prerequisistes

- Docker (See Install Instructions) 

!!! info "Docker install instructions" 
    Settings for install:
    - SELECT Allow Windows Containers to be used with this installation
    - DESELECT Use WSL 2 instead of Hyper-V (On Delft University of Technology PCs, these have outdated/inactive WSL)

On TUD devices disable Use WSL2 engine
https://docs.gitlab.com/runner/install/windows
