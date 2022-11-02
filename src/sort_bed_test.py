# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from bed import BedLine
from sort_bed import sort_chr


def test_sort_chr():
    """Test sort_chr actually sorts a general case"""
    bedlines = [
        BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='foo'),
        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz')
        ]
    expected = [
        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz'),
        BedLine(chrom='chr1', chrom_start=20100, chrom_end=20101, name='foo')
        ]
    assert sort_chr(bedlines) == expected

def test_sort_chr_equal():
    """Test sort_chr deals with features with equal start and end"""
    bedlines = [
        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='foo'),
        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz')
        ]
    expected = [
        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='baz'),
        BedLine(chrom='chr1', chrom_start=600, chrom_end=601, name='foo')
        ]
    assert sort_chr(bedlines) == expected

def test_sort_chr_general_case():
    """Test sort_chr works with a general case"""
    bedlines = [
        BedLine(chrom='chr1', chrom_start=600, chrom_end=700, name='foo'),
        BedLine(chrom='chr1', chrom_start=600, chrom_end=650, name='baz')
        ]
    expected = [
        BedLine(chrom='chr1', chrom_start=600, chrom_end=650, name='baz'),
        BedLine(chrom='chr1', chrom_start=600, chrom_end=700, name='foo')
        ]
    assert sort_chr(bedlines) == expected