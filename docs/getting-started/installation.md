

[poreFlow][poreflow_code] is written in Python and C++, and is published as a [Python package]. We recommend to use a Python _virtual environment_ when installing [with `pip`][with-pip] or [with `uv`][with-uv]. Both options automatically install all necessary dependencies alongside Zensical.

Below, you'll find instructions to install poreFlow on your personal computer.

## Prerequisites

### Operating system

poreFlow is officially supported for macOS Tahoe 26 and Windows 11. For these operating systems, there are pre-built [binary distributions][wheels] of poreFlow wheels

??? note "I have a different OS/version"
    If you are using another OS version, don't worry, you can use poreFlow too. Instead of using the pre-built binary, you can build from source.

    - For MacOS, just follow the instructions below. 
    - If you are using Windows 10, or Windows on an ARM machine, check out the [Developer Install][poreflow-dev-install]
    - For general Linux distributions, install `uv` and follow steps below.

### Python
To install poreFlow you will need Python installed. If you do not have Python on your computer, 
we recommend you follow the [Python Setup and Usage] instructions for your operating system provided on the
[Python website]. Here, follow the instructions for just installing Python.

??? warning "If you are using Anaconda/Miniconda"

    ...Dont? No just kidding.

    If you already have Anaconda/Miniconda installed on your system, 
    Python is already available on your computer. You can skip this step. 
    
    Note that we do not officially support installing on machines with _conda_,
    but members of the Cees Dekker lab are welcome to contact us for assistance 
    to make it work.

    Some tips on installing

    === ":material-apple: macOS"
        In your Terminal Window, run source deactivate to first deactivate _conda_ 
        before installing.

    === ":fontawesome-brands-windows: Windows"

        In your Anaconda Prompt, run deactivate before installing. Alternatively, 
        just use Windows PowerShell.

    === ":material-linux: Linux"

        In your Terminal Window, run source deactivate to first deactivate _conda_ 
        before installing.
        

### A package manager

We recommend installing the [`uv`][uv] package manager, which is a modern and fast package/project manager. 
This will handle the installation of poreFlow, and allow for you to easily add extra packages
needed for your use case. Install `uv` by following the [installation instructions][uv-install].

!!! note "Using just `pip`"
    Installing poreFlow using `pip` only is supported, so go ahead. It is the simplest option 
    to install poreFlow on your system, but we recommend users in the Cees Dekker lab to 
    use `uv`.


## Creating a virtual environment

We recommend installing in a [virtual environment][Python venv] which isolates the 
packages used in a project from the overall Python installation. 

??? tip "About virtual environments"
    
    Typically, this virtual 
    environment is created in the folder of your project:
    
    ```
    username
    └─ my-project
        ├─  .venv
        │     └─ # Packages go here
        ├─  README.md
        ├─  my-code.py
        └─  my-notebook.ipynb
    ```
    
    To create a virtual environment, make sure your working directory is set to 
    your project folder. In the example above, the project folder `my-project` is in the home 
    directory, so we set the working directory to the project folder using:
    
    ```shell
    cd my-project
    ```
    
    Follow the instructions below to create the virtual environment.

    You only need to create the virtual environment once. After creating, you will only 
    need to [activate][Activate-venv] it each time you work in a new terminal. 


[Activate-venv]: #activating-the-virtual-environment

```shell linenums="1" title="Initializing a project and creating a virtual environment"
uv init --python 3.11
uv venv 
```

!!! warning "WIP, supported Python versions"

    poreFlow has been released on PyPi, but for now we are only 
    creating pre-built binaries for Python 3.11. 
    Versions for python 3.11+ coming soon!


## Activating the virtual environment

To activate the virtual environment:

=== ":material-apple: macOS"

    ``` linenums="2" title="Activating a virtual environment"
    source .venv/bin/activate
    ```

=== ":fontawesome-brands-windows: Windows"

    ``` linenums="2" title="Activating a virtual environment"
    .venv\Scripts\activate
    ```

=== ":material-linux: Linux"

    ``` linenums="2" title="Activating a virtual environment"
    source .venv/bin/activate
    ```


## Installing poreFlow

Poreflow can now be installed stand-alone using ``uv``
```shell linenums="3" title="Installing poreFlow"
uv add poreflow
```

## Developer install

If you want to develop, extend, or modify poreFlow, install as a developer 
using the instructions on the [Contributing page][poreflow-dev-install].


[poreflow_code]: https://gitlab.tudelft.nl/xiuqichen/poreFlow
[with-pip]: #install-with-pip
[with-uv]: #install-with-uv
[Python package]: https://pypi.org/project/poreflow
[Python venv]: https://docs.python.org/3/library/venv.html
[Python Setup and Usage]: https://docs.python.org/3/using
[Python website]: https://www.python.org/
[uv]: https://docs.astral.sh/uv/
[uv-install]: https://github.com/astral-sh/uv?tab=readme-ov-file#installation
[Using Python's pip to Manage Your Projects' Dependencies]: https://realpython.com/what-is-pip/
[poreflow-dev-install]: ../developers/installation/#installation-from-source
[wheels]: https://packaging.python.org/en/latest/specifications/binary-distribution-format/