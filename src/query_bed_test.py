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
    x = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(x, 1, 10) == x
    assert extract_region(x, 2, 5) == x
    x = [BedLine("chr1", 2, 3, "foo"), BedLine("chr1", 4, 5, "foo")]
    assert extract_region(x, 2, 5) == x
    assert extract_region(x, 1, 10) == x    

def test_empty_chr():
    x = []
    assert extract_region(x, 1, 10) == x

def test_empty_query():
    x = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(x, 20, 100) == []

def test_query_wrong():
    x = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert not extract_region(x, 2, 2)

def test_one_feature():
    x = [ BedLine("chr1", 2, 3, "foo"),  BedLine("chr1", 4, 5, "foo")]
    assert extract_region(x, 2, 4) == [ BedLine("chr1", 2, 3, "foo") ]