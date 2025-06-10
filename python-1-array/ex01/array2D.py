#!/usr/bin/env python3.10
# Allowed functions : numpy or any lib of table manipulation

import numpy as np

# def slice_me(family: list, start: int, end: int) -> list:
#     print("family: ", family, type(family))
#     print("start: ", start, type(start))
#     print("end: ", end, type(end))
#     sliced_family = family[start:end]
#     print("sliced_family -> ", sliced_family)
#     original_sliced_family = family[slice(start, end)]
#     print("original_sliced_family -> ", original_sliced_family)
#     return ([sliced_family])

def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("family must be a list of lists")

    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a list of lists")

    if len(family) == 0:
        raise ValueError("family must not be empty")

    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError("All rows must have the same length")

    print(f"My shape is : ({len(family)}, {row_length})")

    # slice nesnesi kullanılarak kesim yapılır
    slicer = slice(start, end)
    new_family = family[slicer]

    print(f"My new shape is : ({len(new_family)}, {row_length})")

    return new_family

# def slice_me(family: list, start: int, end: int) -> list:
#     """Slices a 2D list and prints shapes before and after slicing."""

#     # Check input shape
#     original_shape = (len(family), len(family[0]) if family else 0)
#     print(f"My shape is : {original_shape}")

#     # Perform slicing
#     sliced = family[start:end]

#     # Output new shape
#     new_shape = (len(sliced), len(sliced[0]) if sliced else 0)
#     print(f"My new shape is : {new_shape}")

#     return sliced
