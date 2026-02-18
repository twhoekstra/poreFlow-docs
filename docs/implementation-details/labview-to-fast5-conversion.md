# Converting U-Tube (LabView) data to Fast5


## Rationale

Ideally we want a single file format for both the in-house UTube and MinION devices that
are used in the CD lab.

The U-Tube uses LabView for data acquistion and stores measurements as ``.dat`` files while the
ONT MinION stores the data in ``.fast5`` files.

As the MinION is multi-channeled, stores a lot of metadata, and supports storing events and reads on ``.fast5`` files.
The ``.dat`` files used of the U-Tube only allow for the storage a single channel of raw data
in addition to some metadata.

Instead of creating a [third format](https://xkcd.com/927) into which we convert both, it
is more sensible to use the  ``.fast5`` format as a universal format thanks to its many features.

## Method

To do so, we need to convert the ``.dat``  files into ``.fast5`` files. Both formats quantized
the current/voltage signal $y_k$ to some integer $k$ stored in the file.

For the U-Tube, the conversion for signal from stored integers $k$ is as follows:

$$
y_k = (c_0 + c_1 k+c_2x^2) \cdot \frac{1000}{\alpha \beta}
$$

with parameters $c_0, c_1, c_2, \alpha \beta$ stored in the metadata of the ``.dat`` file.
Note that parameter $c_2$ is always assumed to be zero, so this conversion can be simplified
to the linear conversion:

$$
y_k = (c_0 + c_1 k) \cdot \frac{1000}{\alpha \beta}
$$
The ONT devices also have a similar linear conversion between the stored integers to the
signal, but with different parameters:

$$
y_k = (\textrm{offset} + k) \cdot \frac{\textrm{range}}{\textrm{digitalization}}
$$
Like in the U-Tube, these parameters are stored in the metadata to allow for conversion
of the files data to the measured signal. This means that we can store the same integer
values $k` of the ``.dat`` file onto the ``.fast5`` file, as long as we include
the correct parameters for conversion, which we can algebraically derive as:

$$
\textrm{offset} = \frac{c_0}{c_1}, \;\; \textrm{range} = 1000c_1, \;\; \textrm{digitalization} = \alpha \beta
$$

