"""Task 3: Constants, variables and naming conventions"""

# Constants (UPPERCASE by convention)
BASE_RATE = 30.00
BASE_FAT = 3.5
BASE_SNF = 8.5
FAT_ADJUSTMENT = 0.40
SNF_ADJUSTMENT = 0.30
STEP_SIZE = 0.1

print("--- Dynamic typing ---")
value = 10
print(value, type(value))
value = "Morning"
print(value, type(value))

print("\n--- Multiple assignment and swapping ---")
a, b = 10, 20
print("Before swapping:", a, b)
a, b = b, a
print("After swapping:", a, b)

print("\n--- Program using constants ---")
litres = 10.5
fat = 4.2
snf = 8.7

fat_steps = round((fat - BASE_FAT) / STEP_SIZE)
snf_steps = round((snf - BASE_SNF) / STEP_SIZE)
rate_per_litre = BASE_RATE + fat_steps * FAT_ADJUSTMENT + snf_steps * SNF_ADJUSTMENT
payment = litres * rate_per_litre

print(f"Fat steps       : {fat_steps}")
print(f"SNF steps       : {snf_steps}")
print(f"Rate per litre  : Rs {rate_per_litre:.2f}")
print(f"Payment         : Rs {payment:.2f}")

print("\n--- Dictionary-based rate card ---")
rate_card = {"base_rate": 30.00, "fat_adjustment": 0.40, "snf_adjustment": 0.30}
print("Rate card:", rate_card)
print("Fat adjustment from dictionary:", rate_card["fat_adjustment"])

print("\nComplexity: fixed number of operations -> O(1) time, O(1) auxiliary space")
