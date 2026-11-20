"""Task 9: Complete milk payment calculator (uses milkrate.py)"""
from milkrate import rate_per_litre, payout, valid_input, ten_day_total

DAYS = 10


def read_entry(day):
    """Read one day's entry; return (litres, fat, snf) or None if invalid."""
    try:
        litres = float(input(f"Day {day} - litres: "))
        fat = float(input(f"Day {day} - fat %: "))
        snf = float(input(f"Day {day} - SNF %: "))
    except ValueError:
        print("Invalid input: numbers only.")
        return None
    if not valid_input(litres, fat, snf):
        print("Invalid input: litres must be > 0, fat 2.0-7.0, SNF 7.0-10.0.")
        return None
    return litres, fat, snf


def main():
    farmer_id = input("Farmer ID: ").strip()
    payments = []
    day = 1
    while day <= DAYS:
        entry = read_entry(day)
        if entry is None:
            continue                      # ask the same day again
        litres, fat, snf = entry
        pay = payout(litres, fat, snf)
        payments.append(pay)
        print(f"  Rate Rs {rate_per_litre(fat, snf):.2f}/L   Payment Rs {pay:.2f}")
        day += 1
    print(f"\nFarmer {farmer_id}: total for {DAYS} days = Rs {ten_day_total(payments):.2f}")


if __name__ == "__main__":
    main()
