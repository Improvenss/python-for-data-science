#!/usr/bin/env python3.10
from give_bmi import give_bmi, apply_limit

# height = [2.71, 1.15]
# weight = [165.3, 38.4]
height = [0]
weight = [0]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# Expected output:
# $> python tester.py
# [22.507863455018317, 29.0359168241966] <class'list'>
# [False, True]
# $>