





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


