"""Task 1: Payment Calculator for a Village Milk Co-operative"""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_ADJUSTMENT = Decimal("0.40")     # per 0.1 % fat
SNF_ADJUSTMENT = Decimal("0.30")     # per 0.1 % SNF
STEP = Decimal("0.1")
DAYS = 10


def money(x):
    return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def read_number(prompt, low=None, high=None, must_be_positive=False):
    """Keep asking until a valid number is entered."""
    while True:
        try:
            value = Decimal(input(prompt).strip())
        except Exception:
            print("  Invalid input: please enter a number.")
            continue
        if must_be_positive and value <= 0:
            print("  Quantity must be greater than zero.")
        elif low is not None and not (low <= value <= high):
            print(f"  Value must be between {low} and {high}.")
        else:
            return value


def read_shift():
    while True:
        shift = input("  Shift (Morning/Evening): ").strip().capitalize()
        if shift in ("Morning", "Evening"):
            return shift
        print("  Invalid shift: type Morning or Evening.")


def main():
    print("=== Village Milk Co-operative Payment Calculator ===")
    farmer_id = input("Farmer ID: ").strip()
    while not farmer_id:
        farmer_id = input("Farmer ID cannot be empty. Farmer ID: ").strip()

    total = Decimal("0")
    for day in range(1, DAYS + 1):
        print(f"\n--- Day {day} ---")
        shift = read_shift()
        litres = read_number("  Milk quantity (litres): ", must_be_positive=True)
        fat = read_number("  Fat % (2.0 - 7.0): ", Decimal("2.0"), Decimal("7.0"))
        snf = read_number("  SNF % (7.0 - 10.0): ", Decimal("7.0"), Decimal("10.0"))

        fat_steps = (fat - BASE_FAT) / STEP
        snf_steps = (snf - BASE_SNF) / STEP
        rate = BASE_RATE + fat_steps * FAT_ADJUSTMENT + snf_steps * SNF_ADJUSTMENT
        payment = money(litres * rate)
        total += payment

        print(f"  Farmer {farmer_id} | {shift} shift")
        print(f"  Rate per litre : Rs {money(rate)}")
        print(f"  Payment        : Rs {payment}")

    print("\n" + "=" * 40)
    print(f"Total payment for {DAYS} days (Farmer {farmer_id}): Rs {total}")


if __name__ == "__main__":
    main()
