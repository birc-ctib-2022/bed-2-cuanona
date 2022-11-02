# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from bed import BedLine
from merge_bed import is_BedLine_before, merge_sort_generator


def test_different_chr():
    x = BedLine("chr1", 1, 2, "foo")
    y = BedLine("chr0", 10, 20, "foo")
    assert not is_BedLine_before(x, y)

def test_different_start():
    x = BedLine("chr1", 1, 2, "foo")
    y = BedLine("chr1", 10, 20, "foo")
    assert is_BedLine_before(x, y)

def test_different_end():
    x = BedLine("chr1", 10, 20, "foo")
    y = BedLine("chr0", 10, 12, "foo")
    assert not is_BedLine_before(x, y)


def test_simple_merge():
    x = [ BedLine("chr1", 1, 2, "foo"),  BedLine("chr2", 1, 2, "foo")]
    y = [ BedLine("chr1", 5, 10, "foo"),  BedLine("chr3", 1, 2, "foo")]
    expected = [ 
        BedLine("chr1", 1, 2, "foo"),  BedLine("chr1", 5, 10, "foo"),
        BedLine("chr2", 1, 2, "foo"), BedLine("chr3", 1, 2, "foo")]
    observed = [elem for elem in merge_sort_generator(x, y)]
    assert expected == observed

def test_diff_length_merge():
    x = [ BedLine("chr1", 1, 2, "foo"),  BedLine("chr2", 1, 2, "foo")]
    y = [ BedLine("chr1", 5, 10, "foo"),  BedLine("chr3", 1, 2, "foo"), BedLine("chr4", 1, 2, "foo")]
    expected = [ 
        BedLine("chr1", 1, 2, "foo"),  BedLine("chr1", 5, 10, "foo"),
        BedLine("chr2", 1, 2, "foo"), BedLine("chr3", 1, 2, "foo"),
         BedLine("chr4", 1, 2, "foo")]
    observed = list(merge_sort_generator(x, y))
    assert expected == observed