from bed import BedLine

def extract_region(features: list[BedLine],
                   start: int, end: int) -> list[BedLine]:
    """Extract region chrom[start:end] and write it to outfile."""
    index_start = index_stop = binary_search_region_start(features, start)
    for i in range(index_start, len(features)):
        if features[i].chrom_start >= end:
            break
        index_stop += 1
    return features[index_start:index_stop]

def is_overlapping(interval_1: tuple[int,int], interval_2: tuple[int,int]) -> bool:
    """Check if two intervals are overlapping
    >>> is_overlapping((1, 10), (2, 5))
    True
    """
    # Credits to Thomas Maillund :)
    return max(interval_1[0], interval_2[0]) < min(interval_1[1], interval_2[1])

def is_feature_in(feat: BedLine, start: int, end: int):
    """Check if a bedline is in a given interval
    >>> is_feature_in(BedLine("chr1", 0, 3, "foo"), 0, 10)
    True
    """
    interval = (feat.chrom_start, feat.chrom_end)
    return is_overlapping(interval, (start, end))

def binary_search_region_start(bed_lines: list[BedLine], start: int):
    """
    Find first index in a BedLine list for which the chromosome
    start is equal or greater than a given number."""
    low, high = 0, len(bed_lines)
    while low < high:
        mid = (high + low) // 2
        if bed_lines[mid].chrom_start < start:
            low = mid +1
        else:
            high = mid
    return low