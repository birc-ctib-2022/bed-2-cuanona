from bed import BedLine

def extract_region(features: list[BedLine],
                   start: int, end: int) -> list[BedLine]:
    """Extract region chrom[start:end] and write it to outfile."""
    index_start = binary_search_region_start(features, start)
    filtered = list()
    for i in range(index_start, len(features)):
        feat = features[i]
        if feat.chrom_start >= end:
            break
        filtered.append(feat)
    return filtered

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
    if not bed_lines:
        return 0
    while True:
        mid = (high + low) // 2
        y = bed_lines[mid].chrom_start
        if y == start:
            while bed_lines[mid-1].chrom_start == start:
                mid -= 1
            return mid
        if high - low == 1:
            if y > start:
                return mid
            if y < start:
                return mid + 1
        if  y > start:
            high = mid
        if  y < start:
            low = mid