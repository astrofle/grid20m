# Grid20m

Separates and grids GBO's 20m data.

## Installation
Using pip:

    pip install git+https://github.com/astrofle/grid20m.git

Using `conda`:

    conda create --name grid20m-venv python=3.8
    conda activate grid20m-venv
    conda install -c conda-forge pip
    pip install git+https://github.com/astrofle/grid20m.git

## Use
From a terminal:

   grid20m <input_filename> [-o <output_path>] [-a <channel_averaging_factor>] [--overwrite] [-v <verbosity level>] 

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
