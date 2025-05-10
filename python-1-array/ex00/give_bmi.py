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
    if not isinstance(height, list) or not isinstance(weight, list):
        raise ValueError("Both height and weight must be lists.")
    if len(height) == 0 or len(weight) == 0:
        raise ValueError("Height and weight lists cannot be empty.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    if not all(isinstance(h, (int, float)) and h > 0 for h in height):
        raise ValueError("Height values must be positive numbers.")
    if not all(isinstance(w, (int, float)) and w > 0 for w in weight):
        raise ValueError("Weight values must be positive numbers.")
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

def main():
    """
    Main function for testing purposes.
    """
    try:
        # height = [2.71, 1.15]
        # weight = [165.3, 38.4]
        height = [2.71, 1.15, 11.1]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

# give_bmi fonksiyonunuz, girdide 2 tam sayı veya kayan noktalı sayı
#  listesi alır ve BMI değerlerinin bir listesini döndürür.
# apply_limit fonksiyonunuz, bir tam sayı veya kayan noktalı sayı
#  listesi ve bir limiti temsil eden bir tam sayıyı parametre olarak
#  kabul eder. Boolean'lardan oluşan bir liste döndürür
#  (Limitin üzerindeyse True). Listeler aynı boyutta değilse, int veya
#  float değilse hata durumlarını ele almanız gerekir...
if __name__ == "__main__":
    main()

# What is BMI?
#  BMI = Body Mass Index = Vucut kitle indexi