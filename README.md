# Grid20m

Separates and grids GBO's 20m data.

## Installation

    pip install grid20m 

## Use
From a terminal:

    grid20m <input_filename> [-o <output_path>] [-a <channel_averaging_factor>] [--overwrite] [-v <verbosity_level>] [--pixelwidth <pixel_width_in_arcsec>] [--size <horizontal_size> <vertical_size>]

this will produce a series of cubes, as FITS files.
The number of cubes produced depends on how many 
polarizations and spectral windows are present in 
the input file.

## Acknowledgments
If using `grid20m` in your work, please acknowledge the following packages:<br>
[dysh](https://github.com/GreenBankObservatory/dysh)<br>
[gbtgridder](https://github.com/GreenBankObservatory/gbtgridder)<br>
`grid20m` was developed by P. Salas (psalas@nrao.edu).
