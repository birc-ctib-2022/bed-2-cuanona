from bed import BedLine


def binary_search_region_start(x: list[BedLine], start: int, low = None, high = None):
    if low is None:
        low, high = 0, len(x)
    mid = (high + low) // 2
    y = x[mid].chrom_start
    if y == start:
        return mid
    if high - low == 1:
        if y > start:
            return mid
        if y < start:
            return mid + 1
    if  y > start:
        return binary_search_region_start(x, start, low, mid)
    if  y < start:
        return binary_search_region_start(x, start, mid, high)