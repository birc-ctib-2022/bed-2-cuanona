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

def is_overlapping(x: tuple[int,int], y: tuple[int,int]) -> bool:
    # Credits to Thomas Maillund :)
    return max(x[0], y[0]) < min(x[1], y[1])

def is_feature_in(feat: BedLine, start: int, end: int):
    interval = (feat.chrom_start, feat.chrom_end)
    return is_overlapping(interval, (start, end))

def binary_search_region_start(x: list[BedLine], start: int, low = None, high = None):
    low, high = 0, len(x)
    if not x:
        return 0
    while True:
        mid = (high + low) // 2
        y = x[mid].chrom_start
        if y == start:
            while x[mid-1].chrom_start == start:
                mid -= 1
            return mid
        if high - low == 1:
            if y > start:
                return mid
            if y < start:
                return mid + 1
        if  y > start:
            low, high = low, mid
        if  y < start:
            low, high = mid, high