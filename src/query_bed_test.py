# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import random
from bed import BedLine
from query_bed import extract_region
from region_binary_search import is_feature_in
from sort_bed import sort_chr

def generate_random_snp() -> BedLine:
    start = random.randint(0, 6000)
    return BedLine("", start, start + 1, "")

def test_extract_region() -> None:
    for _ in range(1000):
        size = random.randint(0, 20)
        start = random.randint(0, 6000)
        end = start + random.randint(0, 6000 - start)
        features = sort_chr([generate_random_snp() for _ in range(size)])
        expected = [feat for feat in features if is_feature_in(feat, start, end)]
        assert expected == extract_region(features, start, end)

def test_happy_path():
    bed_lines = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(bed_lines, 1, 10) == bed_lines
    assert extract_region(bed_lines, 2, 5) == bed_lines
    bed_lines = [BedLine("chr1", 2, 3, "foo"), BedLine("chr1", 4, 5, "foo")]
    assert extract_region(bed_lines, 2, 5) == bed_lines
    assert extract_region(bed_lines, 1, 10) == bed_lines    

def test_empty_chr():
    bed_lines = []
    assert extract_region(bed_lines, 1, 10) == bed_lines

def test_empty_query():
    bed_lines = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert not extract_region(bed_lines, 20, 100)

def test_query_wrong():
    bed_lines = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert not extract_region(bed_lines, 2, 2)

def test_one_feature():
    bed_lines = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(bed_lines, 2, 4) == [ BedLine("chr1", 2, 3, "foo") ]