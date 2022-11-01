from bed import BedLine
import random
from region_binary_search import binary_search_region_start, extract_region, is_feature_in
from sort_bed import sort_chr

def test_empty_list()-> None:
    x = []
    assert binary_search_region_start(x, start = 5) == 0
def test_lower_bound_exact() -> None:
    x = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(x, start = 0) == 0

def test_lower_bound_non_exact() -> None:
    x = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(x, start = 1) == 1

def test_upper_bound_exact() -> None:
    x = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(x, start = 9) == 5


def test_upper_bound_non_exact() -> None:
    x = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(x, start = 10) == 6

def test_general_case_exact() -> None:
    x = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(x, start = 5) == 2

def test_general_case_non_exact() -> None:
    x = [
        BedLine("chr1", 0, 3, "foo"),
        BedLine("chr1", 3, 3, "foo"),
        BedLine("chr1", 5, 3, "foo"),
        BedLine("chr1", 6, 3, "foo"),
        BedLine("chr1", 7, 3, "foo"),
        BedLine("chr1", 9, 3, "foo")
        ]
    assert binary_search_region_start(x, start = 4) == 2
