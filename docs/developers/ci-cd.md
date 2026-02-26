# CI/CD

poreFlow uses Continuous Integration/Continuous Deployment (CI/CD) to automate 
package testing, building, and packaging.

## Windows runner:

We are creating Windows runner with a shell executor. Pitfalls!

We use the Docker executor for Windows.

### Prerequistes
- Git 
- `uv` 

!!! note "On the install"
    Use default installs for both git and `uv`. Both will install at the user level


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
10. As an executor, select "shell"

This should create a `config.toml`. Make sure it looks like:

```toml linenums="1"

```

11. Install and start the runner

```shell linenums="3"
.\gitlab-runner.exe install
.\gitlab-runner.exe start
```

## Windows services

Use run as administrator
"gitlab-runner"

[Windows runner reference]: https://docs.gitlab.com/runner/install/windows
[Runner download]: https://s3.dualstack.us-east-1.amazonaws.com/gitlab-runner-downloads/latest/binaries/gitlab-runner-windows-amd64.exe
[Elevated command prompt]: https://learn.microsoft.com/en-us/powershell/scripting/windows-powershell/starting-windows-powershell?view=powershell-7.4#with-administrative-privileges-run-as-administrator
[MSVS docs]: https://learn.microsoft.com/en-us/visualstudio/install/build-tools-container?view=visualstudio