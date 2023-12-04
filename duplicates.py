def remove_duplicates(sequence):
    removed = set()

    for item in sequence:
        removed.add(item)
    print(removed)
    return removed

# Test

remove_duplicates([2, 3, 2, 4, 5, 3, 6, 7,11,12, 5])