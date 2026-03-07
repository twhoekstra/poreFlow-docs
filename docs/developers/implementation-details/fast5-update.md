# On the `fast5_research` dependency

The original `fast5_research` module hasn't been updated in 3 years, and has old dependencies. Instead of opting to vendorize the `fast5_research` code, we created a fork and updated it. This allows us to read/write `.fast5` files used in our ONT measurements. Note that the most important part of the API for this is `fast5_research.BulkFast5`.

`fast5_research` is bundled in poreflow, so does not need to be installed seperately.

## Process

Thankfully, a lot of the `fast5_research` was tested. This meant we could quickly clean up and fix the source code using an LLM (in this case Gemini CLI). Gemini was not able to fix all bugs, so some manual research into the module was needed to fix it completely. Once the source code was fixed, the tests were reformatted for clarity.

## Changes to the module

- Bugfixes
- Dependency updates
- `progressbar` dependency was replaced by `tqdm`
- Tests were rewritten to use the cleaner `pytest` rather than `unittest`

