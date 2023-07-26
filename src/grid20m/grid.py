"""
"""

import sys

from gbtgridder import gbtgridder, gbtgridder_args


def grid(args):
    """
    """
    gbtgridder.gbtgridder(args)


def parse_args(filename, base, average=None, 
               overwrite=False, diameter=20,
               verbose=4):
    """
    """

    sys.argv = [sys.argv[0]]
    sys.argv.append(filename)
    sys.argv.append("-o")
    sys.argv.append(base)
    sys.argv.append("--diameter")
    # Even though this is a float, it 
    # needs to be wrapped as a string.
    sys.argv.append(f"{diameter}")
    if average:
        sys.argv.append("-a")
        sys.argv.append(f"{average}")
    if overwrite:
        sys.argv.append("--clobber")
    sys.argv.append("--autoConfirm")
    sys.argv.append("-v")
    sys.argv.append(f"{verbose}")
    
    return sys.argv


def main(filename, base, average=None, 
         overwrite=False, diameter=20, verbose=4):
    """
    """

    args = parse_args(filename, base, average=average, 
                      overwrite=overwrite, diameter=diameter,
                      verbose=verbose)
    args = gbtgridder_args.parser_args(args, "2.0")
    gbtgridder_args.check_args(args)
    grid(args)

