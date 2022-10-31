"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_line, print_line, BedLine
)


def read_bed_file(f: TextIO) -> list[BedLine]:
    """Read an entire sorted bed file."""
    # Handle first line...
    line = f.readline()
    if not line:
        return []

    res = [parse_line(line)]
    for line in f:
        feature = parse_line(line)
        prev_feature = res[-1]
        assert prev_feature.chrom < feature.chrom or \
            (prev_feature.chrom == feature.chrom and
             prev_feature.chrom_start <= feature.chrom_start), \
            "Input files must be sorted"
        res.append(feature)

    return res

def is_BedLine_before(elem1: BedLine, elem2: BedLine):
    for key in ['chrom', 'chrom_start', 'chrom_end']:
        if getattr(elem1,key) > getattr(elem2,key):
            return False
    return True

def merge_sort_generator(f1: list[BedLine], f2: list[BedLine]) -> BedLine:
    iter1, iter2 = iter(f1), iter(f2)
    for (elem1, elem2) in zip(iter1, iter2):
        if is_BedLine_before(elem1, elem2):
            yield elem1
        yield elem2
    for elem1 in iter1:
        yield elem1
    for elem2 in iter2:
        yield elem2


def merge(f1: list[BedLine], f2: list[BedLine], outfile: TextIO) -> None:
    for elem in merge_sort_generator(f1, f2):
        print_line(elem, outfile)


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(description="Merge two BED files")
    argparser.add_argument('f1', type=argparse.FileType('r'))
    argparser.add_argument('f2', type=argparse.FileType('r'))
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',   # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    features1 = read_bed_file(args.f1)
    features2 = read_bed_file(args.f2)
    merge(features1, features2, args.outfile)


if __name__ == '__main__':
    main()
