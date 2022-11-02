"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from typing import TextIO
from bed import (
    parse_line, print_line, BedLine
)


def read_bed_file(file: TextIO) -> list[BedLine]:
    """Read an entire sorted bed file."""
    # Handle first line...
    line = file.readline()
    if not line:
        return []

    res = [parse_line(line)]
    for line in file:
        feature = parse_line(line)
        prev_feature = res[-1]
        assert prev_feature.chrom < feature.chrom or \
            (prev_feature.chrom == feature.chrom and
             prev_feature.chrom_start <= feature.chrom_start), \
            "Input files must be sorted"
        res.append(feature)

    return res

def is_bedline_before(elem1: BedLine, elem2: BedLine) -> bool:
    """Check if a BedLine tuple is before another
    >>> is_BedLine_before(BedLine("chr1", 1, 2, "foo"),BedLine("chr1", 5, 6, "foo"))
    True
    """
    for key in ['chrom', 'chrom_start', 'chrom_end']:
        if getattr(elem1,key) > getattr(elem2,key):
            return False
    return True

def merge_sort_generator(list_1: list[BedLine], list_2: list[BedLine]) -> list[BedLine]:
    """It merges two sorted list and yields elements."""
    iter1, iter2 = iter(list_1), iter(list_2)
    for (elem1, elem2) in zip(iter1, iter2):
        if is_bedline_before(elem1, elem2):
            yield elem1
        yield elem2
    for elem1 in iter1:
        yield elem1
    for elem2 in iter2:
        yield elem2


def merge(list_1: list[BedLine], list_2: list[BedLine], outfile: TextIO) -> None:
    """Merge 2 BedLine list and write the result into an output file."""
    for elem in merge_sort_generator(list_1, list_2):
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
