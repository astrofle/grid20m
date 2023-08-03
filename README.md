# Grid20m

Separates and grids GBO's 20m data.

## Installation
Using `conda`:

    conda create --name grid20m-venv python=3.8
    conda activate grid20m-venv
    conda install -c conda-forge pip
    pip install numpy scipy cython
    pip install git+https://github.com/GreenBankObservatory/gbtgridder.git@release_2.0
    pip install git+https://github.com/astrofle/grid20m.git

## Use
From a terminal:

   grid20m <input_filename> [-o <output_path>] [-a <channel_averaging_factor>] [--overwrite] [-v <verbosity level>] [--pixelwidth <pixel_width_in_arcsec>] [--size <X> <Y>]

this will produce a series of cubes, as FITS files.
The number of cubes produced depends on how many 
polarizations and spectral windows are present in 
the input file.

## Acknowledgments
If using `grid20m` in your work, please acknowledge the following packages:<br>
[dysh](https://github.com/GreenBankObservatory/dysh)<br>
[gbtgridder](https://github.com/GreenBankObservatory/gbtgridder)<br>
[cygrid](https://github.com/bwinkel/cygrid)<br>
`grid20m` was developed by P. Salas (psalas@nrao.edu).
