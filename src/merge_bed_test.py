# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from bed import BedLine
from merge_bed import is_bedline_before, merge_sort_generator


def test_different_chr() -> None:
    """Test is BedLine_before with different chromosomes"""
    x = BedLine("chr1", 1, 2, "foo")
    y = BedLine("chr0", 10, 20, "foo")
    assert not is_bedline_before(x, y)


def test_different_start() -> None:
    """Test is BedLine_before with different start"""
    x = BedLine("chr1", 1, 2, "foo")
    y = BedLine("chr1", 10, 20, "foo")
    assert is_bedline_before(x, y)


def test_different_end() -> None:
    """Test is BedLine_before with different end"""
    x = BedLine("chr1", 10, 20, "foo")
    y = BedLine("chr0", 10, 12, "foo")
    assert not is_bedline_before(x, y)


def test_simple_merge() -> None:
    """Test simple merge"""
    x = [BedLine("chr1", 1, 2, "foo"),  BedLine("chr2", 1, 2, "foo")]
    y = [BedLine("chr1", 5, 10, "foo"),  BedLine("chr3", 1, 2, "foo")]
    expected = [
        BedLine("chr1", 1, 2, "foo"),  BedLine("chr1", 5, 10, "foo"),
        BedLine("chr2", 1, 2, "foo"), BedLine("chr3", 1, 2, "foo")]
    observed = [elem for elem in merge_sort_generator(x, y)]
    assert expected == observed


def test_diff_length_merge() -> None:
    """Test merge with different lenght"""
    list_1 = [BedLine("chr1", 1, 2, "foo"),  BedLine("chr2", 1, 2, "foo")]
    list_2 = [BedLine("chr1", 5, 10, "foo"),  BedLine(
        "chr3", 1, 2, "foo"), BedLine("chr4", 1, 2, "foo")]
    expected = [
        BedLine("chr1", 1, 2, "foo"),  BedLine("chr1", 5, 10, "foo"),
        BedLine("chr2", 1, 2, "foo"), BedLine("chr3", 1, 2, "foo"),
        BedLine("chr4", 1, 2, "foo")]
    observed = list(merge_sort_generator(list_1, list_2))
    assert expected == observed