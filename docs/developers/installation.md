# Installation from source

## Prerequisites

The prerequisites are:

1. A package manager
2. A virtual environment to install packages into (recommended)
3. Git
4. Access to the poreFlow repository
5. Visual Studio Build Tools (Windows only)

You can of course use any package manager you want, but `uv` is recommended thanks to its speed and built-in 
formatting. For installation, follow the [official uv installation steps](https://github.com/astral-sh/uv?tab=readme-ov-file#installation). For instructions on how
to create a virtual environment, check out the 
[Installation](../getting-started/installation/#creating-a-virtual-environment) page.


## Cloning repository

To clone the repository, use:

```shell linenums="1"
git clone https://gitlab.tudelft.nl/xiuqichen/poreFlow.git
```

Ensure you have access to the repository. After cloning, make sure you working directory is set to `poreFlow` before running.

```shell linenums="2"
cd poreFlow
```

## Install dependencies and module
To install, simply run:
```shell linenums="3"
uv sync
```

This, by default makes use of the [lockfile](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile) provided 
in this repository, ensuring you install the same packages as the main developers.

`uv sync` will automatically create a virtual environment. To activate the virtual environment:

=== ":material-apple: macOS"

    ``` linenums="4"
    source .venv/bin/activate
    ```

=== ":fontawesome-brands-windows: Windows"

    ``` linenums="4"
    .venv\Scripts\activate
    ```

=== ":material-linux: Linux"

    ``` linenums="3"
    source .venv/bin/activate
    ```


!!! tip 

    If you are habing trouble installing packages, try deleting the lockfile (`uv.lock`) and re-running
    `uv sync`. `uv` will then install poreflow and it's dependencies from the requirements 
    specified in `pyproject.toml`. It will also install additional developer dependencies 
    such as Jupyter Lab and pytest.

??? info "Installing with ``pip`` instead (not recommended)"
    
    You can also install dependencies and the module by installing the module in editable mode 
    using `pip`.

    ```shell
    uv pip install -e ".[dev]"
    ```