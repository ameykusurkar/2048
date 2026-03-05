def collapse_list(numbers: list[int], reverse: bool = False) -> list[int]:
    """Collapse a row/column by merging adjacent equal tiles toward the front."""
    original_length = len(numbers)

    if reverse:
        numbers = numbers[::-1]
    else:
        numbers = list(numbers)

    # Remove zeros, then merge adjacent equal values
    filtered = [x for x in numbers if x != 0]
    merged: list[int] = []
    i = 0
    while i < len(filtered):
        if i + 1 < len(filtered) and filtered[i] == filtered[i + 1]:
            merged.append(filtered[i] * 2)
            i += 2
        else:
            merged.append(filtered[i])
            i += 1

    # Pad with zeros to maintain original length
    merged.extend([0] * (original_length - len(merged)))

    if reverse:
        merged = merged[::-1]

    return merged
