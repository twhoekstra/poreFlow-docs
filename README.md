# poreFlow Documentation

Repository for documentation for the [poreFlow module]. 
Hosted on GitHub pages, check it out [here][poreFlow docs].

## Developers

### Install

After `git clone` this repo, run the following:

```shell
cd poreFlow-docs
uv sync
source .venv/bin/activate
```

### Use
```shell
zensical serve
```

[poreFlow module]: https://gitlab.tudelft.nl/xiuqichen/poreFlow
[poreFlow docs]: https://twhoekstra.github.io/poreFlow-docs/

## Troubleshooting

### 404 error
Check whether the build artefacts contain `index.html`. If not, check the log files. 
There is probably an error when building (`zensical build --clean`). Currently, 
Zensical doesn't support a strict build, so the build might exit without errors.