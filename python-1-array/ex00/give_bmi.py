#!/usr/bin/env python3.10
# Allowed functions : numpy or any lib of table manipulation
import numpy as np

# LINK: https://www.tradingcode.net/python/math/exponents/
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI values for given heights and weights.

    :param height: List of heights in meters.
    :param weight: List of weights in kilograms.
    :return: List of BMI values.
    :raises ValueError: If the input lists are not of the same length, contain invalid types, or are empty.
    """
    if not isinstance(height, list):
        raise TypeError("expected 'height' to be a list.")
    if not isinstance(weight, list):
        raise TypeError("expected 'weight' to be a list.")
    if not height:
        raise ValueError("The 'height' list cannot be empty.")
    if not weight:
        raise ValueError("The 'weight' list cannot be empty.")
    if len(height) != len(weight):
        raise ValueError("'height' and 'weight' lists must be of equal length.")
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("all elements in 'height' must be int or float.")
    if not all(h > 0 for h in height):
        raise ValueError("all elements in 'height' must be positive numbers.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("all elements in 'weight' must be int or float.")
    if not all(w > 0 for w in weight):
        raise ValueError("all elements in 'weight' must be positive numbers.")
    # bmi_values = np.array(weight) / np.array(height) ** 2
    bmi_values = np.array(weight) / pow(np.array(height), 2)
    return bmi_values.tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if BMI values exceed a given limit.

    :param bmi: List of BMI values.
    :param limit: Limit value to compare against.
    :return: List of booleans (True if BMI is above the limit, False otherwise).
    :raises ValueError: If the input is invalid.
    """
    if not isinstance(bmi, list) or not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("BMI list must contain only numbers.")
    if not isinstance(limit, int):
        raise ValueError("Limit must be an integer.")
    return [b > limit for b in bmi]

# def main():
#     try:
#         height = [2.71, 1.15]
#         weight = [165.3, 38.4]
#         # height = [2.71, 1.15, 11.1]
#         # weight = [165.3, 38.4]
#         bmi = give_bmi(height, weight)
#         print(bmi, type(bmi))
#         print(apply_limit(bmi, 26))
#     except ValueError as ve:
#         print(f"Error: {ve}")
#     except Exception as e:
#         print(f"Error: {e}")

# # give_bmi fonksiyonunuz, girdide 2 tam sayi veya kayan noktali sayi
# #  listesi alir ve BMI degerlerinin bir listesini dondurur.
# # apply_limit fonksiyonunuz, bir tam sayi veya kayan noktali sayi
# #  listesi ve bir limiti temsil eden bir tam sayiyi parametre olarak
# #  kabul eder. Boolean'lardan oluşan bir liste dondurur
# #  (Limitin uzerindeyse True). Listeler ayni boyutta degilse, int veya
# #  float degilse hata durumlarini ele almaniz gerekir...
# if __name__ == "__main__":
#     main()

# What is BMI?
#  BMI = Body Mass Index = Vucut kitle indexi