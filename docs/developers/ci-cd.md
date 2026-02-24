# CI/CD

poreFlow uses Continuous Integration/Continuous Deployment (CI/CD) to automate 
package testing, building, and packaging.

## Windows runner:

### Installing Docker

We use the Docker executor for Windows.

- Docker (See Install Instructions) 

!!! info "Docker install instructions" 
    Settings for install:
    - SELECT Allow Windows Containers to be used with this installation
    - DESELECT Use WSL 2 instead of Hyper-V (On Delft University of Technology PCs, these have outdated/inactive WSL)

After install:
Click to the arrow on the right hand the taskbar of windows
Right click on docker
Slick "Switch to windows containers"

### Creating a Docker Image

To complete all the CI/CD, we want an image with:
- The `uv` package manager
- C++ build tools
- Python

In this section you will create an image containing all these tools. 

!!! note 

    This section is based on the [Microsoft Visual Studio Documentation][MSVS docs]

1. Create a folder named `BuildTools`.
2. In this folder, create a file named `dockerfile` with the following contents:
```dockerfile

```

3. In a terminal, create the image:
```shell linenums="1"
cd BuildTools
docker build -t buildtools:latest -m 2GB .
```


### Installing GitLab Runner for windows

For more info, see the [GitLab docs reference][Windows runner reference].

1. Create a folder somewhere in your system, for example, C:\GitLab-Runner.
2. Download the binary for [64-bit][Runner download] and put it into the folder you created. 
3. Rename the binary to `gitlab-runner.exe`
4. Run an [elevated command prompt][Elevated command prompt]
5. Run the register command:

```shell linenums="1"
cd C:\GitLab-Runner
.\gitlab-runner.exe register
```

6. Enter `gitlab.tudelft.nl` as the GitLab URL
7. Get a runner authentication token from GitLab and enter it
8. Enter the description for the runner.
9. Enter the job tag `windows`
10. As an executor, select "docker-windows"

This should create a `config.toml`. Make sure it looks like:

```toml linenums="1"

```

11. Install and start the runner

```shell linenums="3"
.\gitlab-runner.exe install
.\gitlab-runner.exe start
```


[Windows runner reference]: https://docs.gitlab.com/runner/install/windows
[Runner download]: https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/latest/binaries/gitlab-runner-windows-amd64.exe
[Elevated command prompt]: https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.4#with-administrative-privileges-run-as-administrator
[MSVS docs]: https://learn.microsoft.com/en-us/visualstudio/install/build-tools-container?view=visualstudio