# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_
from bed import BedLine
from region_binary_search import binary_search_region_start

def test_non_unique_start():
    """Test binary search for a start with several features"""
    bed_lines = [
        BedLine("chrom3",	774,	775,	"Feature-148"),
        BedLine("chrom3",	778,	779,	"Feature-125"),
        BedLine("chrom3",	780,	781,	"Feature-401"),
        BedLine("chrom3",	796,	797,	"Feature-515"),
        BedLine("chrom3",	796,	797,	"Feature-646"),
        BedLine("chrom3",	809,	810,	"Feature-335")
        ]
    assert binary_search_region_start(bed_lines, start = 796) == 3

def test_empty_list()-> None:
    """Test binary for empty list"""
    bed_lines: list[BedLine] = list()
    assert binary_search_region_start(bed_lines, start = 5) == 0

def test_lower_bound_exact() -> None:
    """Test binary search for lower exact start"""
    bed_lines = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(bed_lines, start = 0) == 0

def test_lower_bound_non_exact() -> None:
    """Test binary search for non exact lower start"""
    bed_lines = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(bed_lines, start = 1) == 1

def test_upper_bound_exact() -> None:
    """Test binary search for upper exact start"""
    bed_lines = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(bed_lines, start = 9) == 5


def test_upper_bound_non_exact() -> None:
    """Test binary search for upper non exact start"""
    bed_lines = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(bed_lines, start = 10) == 6

def test_general_case_exact() -> None:
    """Test binary search for general case"""
    bed_lines = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(bed_lines, start = 5) == 2

def test_general_case_non_exact() -> None:
    """Test binary search for non exact general case"""
    bed_lines = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(bed_lines, start = 4) == 2
