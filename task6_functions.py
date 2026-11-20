"""Task 6: Organise the logic into functions"""

BASE_RATE = 30.00          # global constants
BASE_FAT = 3.5
BASE_SNF = 8.5
FAT_ADJUSTMENT = 0.40
SNF_ADJUSTMENT = 0.30


def rate_per_litre(fat, snf):
    """Return the rate per litre (fat_steps and snf_steps are local variables)."""
    fat_steps = round((fat - BASE_FAT) / 0.1)
    snf_steps = round((snf - BASE_SNF) / 0.1)
    return BASE_RATE + fat_steps * FAT_ADJUSTMENT + snf_steps * SNF_ADJUSTMENT


def payout(quantity, fat, snf):
    """Return the payment for one delivery."""
    payment = quantity * rate_per_litre(fat, snf)
    return round(payment, 2)


def ten_day_total(payments):
    """Return the total of a list of ten daily payments."""
    return round(sum(payments), 2)


def main():
    entries = [
        (10.0, 3.5, 8.5), (8.5, 4.2, 8.7), (12.0, 3.1, 8.3), (9.0, 3.8, 8.6),
        (11.0, 4.0, 8.5), (10.5, 4.2, 8.7), (7.0, 3.6, 8.4), (13.0, 3.9, 8.6),
        (9.5, 3.5, 8.5), (10.0, 4.1, 8.8),
    ]
    payments = []
    print(f"{'Day':>3} {'Litres':>7} {'Fat':>5} {'SNF':>5} {'Rate':>8} {'Payment':>10}")
    for day, (litres, fat, snf) in enumerate(entries, start=1):
        pay = payout(litres, fat, snf)
        payments.append(pay)
        print(f"{day:>3} {litres:>7} {fat:>5} {snf:>5} "
              f"{rate_per_litre(fat, snf):>8.2f} {pay:>10.2f}")
    print(f"\nTotal for 10 days: Rs {ten_day_total(payments):.2f}")

    # return vs print: the returned value can be reused
    first = payout(10, 3.5, 8.5)
    print("Reused returned value (payment x 2):", first * 2)

    # Lambda alternative (suitable only for very short expressions)
    simple_rate = lambda fat, snf: BASE_RATE + round((fat - BASE_FAT) / 0.1) * FAT_ADJUSTMENT \
        + round((snf - BASE_SNF) / 0.1) * SNF_ADJUSTMENT
    print("Lambda rate for 4.2 / 8.7:", round(simple_rate(4.2, 8.7), 2))


if __name__ == "__main__":
    main()
