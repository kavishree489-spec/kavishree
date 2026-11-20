"""Task 4: Arithmetic expressions, operator precedence and rounding"""
import math

BASE_RATE = 30.00
BASE_FAT = 3.5
BASE_SNF = 8.5
FAT_ADJUSTMENT = 0.40
SNF_ADJUSTMENT = 0.30

litres = 10.5
fat = 4.2
snf = 8.7

fat_steps = (fat - BASE_FAT) / 0.1
snf_steps = (snf - BASE_SNF) / 0.1
print("Raw fat steps :", fat_steps, "(floating-point result)")
print("Raw SNF steps :", snf_steps)

# round() fixes the tiny float errors, e.g. 6.999999999999999 -> 7
fat_steps = round(fat_steps)
snf_steps = round(snf_steps)
print("Fat steps     :", fat_steps)
print("SNF steps     :", snf_steps)

rate = BASE_RATE + (fat_steps * FAT_ADJUSTMENT) + (snf_steps * SNF_ADJUSTMENT)
payment = litres * rate
print(f"Rate per litre: Rs {rate:.2f}")
print(f"Payment       : Rs {payment:.2f}")

print("\n--- Operator precedence ---")
print("2 + 3 * 4   =", 2 + 3 * 4)
print("-2 ** 2     =", -2 ** 2)
print("(-2) ** 2   =", (-2) ** 2)

print("\n--- Rounding methods ---")
for number in (33.4, 33.5, 33.6, -33.5):
    print(f"{number:>6}: round={round(number)}  int={int(number)}  floor={math.floor(number)}")
print("Note: round(2.5) =", round(2.5), "and round(3.5) =", round(3.5),
      "(Python rounds halves to the nearest even number)")

print("\nComplexity: O(1) time, O(1) auxiliary space")
