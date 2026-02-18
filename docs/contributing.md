
## Overview of contribution process

Changes to poreFlow are typically done by members of the Cees Dekker lab. Members first clone the repository to their 
personal computer, then make a branch in which they edit the source code, and then push the local cahnges back up to 
GitLab. When changes are done, the member creates a pull request to incorporate their changes into the codebase.

This page will contain both the style guide for the module, along with instructions to set up your local development 
environment. Note that the style guide below is more of a recommendation than a decree: if write clean code in a 
different style, please go ahead. If you are still looking to learn however, these guidelines might be a good place 
to start.

## Coding conventions

1. **Tested.** All new functionality would ideally include test coverage. For learning more about tests, consult the 
[pytest documentation](https://docs.pytest.org/en/stable/how-to/index.html). Make tests fast.
2. **Documented.** All new functionality must be documented, preferably through these docs along with docstrings
in the source code.
3. **Minimize API changes**. Please minimize changes to the public API. Changes to the public API 
(e.g., class/function/method names and signatures) should not be made lightly, as they can break existing user scripts.

## Code style
1. **Follow the Google Python Style Guide** Consult the 
[Google Style guide](https://google.github.io/styleguide/). To format the code, see the [formatting instructions](#formatting-code).
2. **Google-style docstrings** Write 
[Google-style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) docstrings.

## Installation from source

### Prerequisites

The prerequisites are:

1. A package manager
2. A virtual environment to install packages into (recommended)
3. Git
4. Access to the poreFlow repository

You can of course use any package manager you want, but `uv` is recommended thanks to its speed and built-in 
formatting. For installation, follow the [official uv installation steps](https://github.com/astral-sh/uv?tab=readme-ov-file#installation). For instructions on how
to create a virtual environment, check out the 
[Installation](../getting-started/installation/#creating-a-virtual-environment) page.


### Install dependencies and module

Install dependencies and module by installing the module in editable mode. Make sure you working directory is set 
to `poreFlow` before running:

```shell
uv pip install -e ".[dev]"
```

!!! info

    Installing with the additional dependencies ``dev`` will install packages needed for building this documentation, 
    testing the code, and formatting, along with Jupyter Notebook.

??? info "Installing with ``uv sync`` instead"

    PoreFlow and its dependencies can also be installed using the
    [lockfile](https://docs.astral.sh/uv/concepts/projects/layout/#the-lockfile) provided in this repository. 
    To install, simply run 
    ```shell 
      uv sync
    ```

### Installing `fast5-research` in editable mode (not recommended)
You can also install our fork of the `fast5-research` dependency in editable mode. If it is cloned from the CD 
lab fork [repository](https://gitlab.tudelft.nl/thijnhoekstra/fast5_research) to the same folder as `poreFlow`:

```shell
uv pip install -e "../fast5_research"
```

## Developing with Git

### Creating a branch

To create a branch for a specific feature:

=== "In GitLab"
  
    1. Go to the [poreFlow Issue Board](https://gitlab.tudelft.nl/xiuqichen/poreFlow/-/boards)
    2. In the "Open" tab, create a new issue using the + icon
    3. Add a title. Press enter, a new tab will top up.
    4. Click "Create Merge Request". The source of the new branch will be the "main", a new branch name will be suggested.
    5. Click the "Create Merge Request" button to confirm. A new window will open named "New merge request".
    6. (Optional) Add additional information.
    7. Click the "Create Merge Request" button to confirm.
  
    A new branch has been created. Next update Git and display branches:
    
    ```shell
    git pull
    git -P branch
    ```
    
    The new branch can be checked out using: 
    ```shell
    git checkout x-my-new-branch
    ```
    
    !!! tip
        You can use tab after ``git checkout`` to auto-complete an available branch name.

=== "In a terminal"

    ```
    git checkout -b "my-new-branch"
    ```

### Commiting changes 

```shell
git commit -m "Descriptive message"
git push
```


## Running tests
To test the code for the entire module, make sure you are in the ``poreFlow`` directory and simply run:

```shell
pytest
```
Tests for individual submodules can be found in the ``tests`` folder.

## Formatting code

Formatting is built into `uv`. To run:

```shell
uv format
```