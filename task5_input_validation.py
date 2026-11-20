"""Task 5: User input, type conversion and validation"""

BASE_RATE = 30.00
BASE_FAT = 3.5
BASE_SNF = 8.5
FAT_ADJUSTMENT = 0.40
SNF_ADJUSTMENT = 0.30


def main():
    try:
        litres = float(input("Enter milk quantity (litres): "))
        fat = float(input("Enter fat percentage: "))
        snf = float(input("Enter SNF percentage: "))
    except ValueError:
        print("Invalid numerical input. Please enter numbers only.")
        return

    # Validation using if / elif
    if litres <= 0:
        print("Error: milk quantity must be greater than 0.")
    elif fat < 2.0 or fat > 7.0:
        print("Error: fat percentage must be between 2.0 and 7.0.")
    elif snf < 7.0 or snf > 10.0:
        print("Error: SNF percentage must be between 7.0 and 10.0.")
    else:
        fat_steps = round((fat - BASE_FAT) / 0.1)
        snf_steps = round((snf - BASE_SNF) / 0.1)
        rate = BASE_RATE + fat_steps * FAT_ADJUSTMENT + snf_steps * SNF_ADJUSTMENT
        payment = litres * rate
        print(f"Rate per litre : Rs {rate:.2f}")
        print(f"Payment        : Rs {payment:.2f}")


if __name__ == "__main__":
    main()
