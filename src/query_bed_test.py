# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from bed import BedLine
from query_bed import extract_region


def test_happy_path():
    x = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(x, 1, 10) == x
    assert extract_region(x, 2, 5) == x
    x = y = [ BedLine("chr1", 4, 5, "foo"), BedLine("chr1", 2, 3, "foo")]
    assert extract_region(x, 1, 10) == x
    assert extract_region(x, 2, 5) == x

def test_empty_chr():
    x = []
    assert extract_region(x, 1, 10) == x

def test_empty_query():
    x = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(x, 20, 100) == []

def test_query_wrong():
    x = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(x, 2, 2) == []

def test_one_feature():
    x = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(x, 2, 4) == [ BedLine("chr1", 2, 3, "foo") ]

def test_non_SNP():
    x = [ BedLine("chr1", 2, 8, "foo"),  BedLine("chr1", 4, 7, "foo")]
    assert extract_region(x, 3, 5) == x