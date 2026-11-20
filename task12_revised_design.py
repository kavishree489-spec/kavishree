"""Task 12: Revised design - seasonal rates, two-decimal analyser readings, ten-day bonus"""
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STEP = Decimal("0.1")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
SNF_ADJUSTMENT = Decimal("0.30")

RATE_CARDS = {
    "Original":   {"base_rate": Decimal("30.00"), "fat_adjustment": Decimal("0.40")},
    "April-June": {"base_rate": Decimal("32.00"), "fat_adjustment": Decimal("0.45")},
}
BONUS_THRESHOLD_LITRES = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")


def season_for_month(month):
    """Return 'April-June' for months 4-6, otherwise 'Original'."""
    return "April-June" if 4 <= month <= 6 else "Original"


def rate_per_litre(fat, snf, season="Original"):
    if season not in RATE_CARDS:
        raise ValueError(f"Unknown season: {season}")
    card = RATE_CARDS[season]
    # Readings keep two decimals; steps are rounded to the nearest whole step
    fat_steps = round((Decimal(str(fat)) - BASE_FAT) / STEP)
    snf_steps = round((Decimal(str(snf)) - BASE_SNF) / STEP)
    return card["base_rate"] + fat_steps * card["fat_adjustment"] + snf_steps * SNF_ADJUSTMENT


def payout(quantity, fat, snf, season="Original"):
    amount = Decimal(str(quantity)) * rate_per_litre(fat, snf, season)
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


def bonus(total_litres):
    """Rs 0.50 per litre if the ten-day supply is MORE than 500 litres."""
    total_litres = Decimal(str(total_litres))
    if total_litres > BONUS_THRESHOLD_LITRES:
        return (total_litres * BONUS_PER_LITRE).quantize(CENT, rounding=ROUND_HALF_UP)
    return Decimal("0.00")


def ten_day_total(entries, season="Original"):
    """entries = list of (litres, fat, snf). Returns (payments, bonus, grand_total)."""
    payments = Decimal("0")
    litres_total = Decimal("0")
    for litres, fat, snf in entries:
        payments += payout(litres, fat, snf, season)      # running total -> O(1) extra space
        litres_total += Decimal(str(litres))
    extra = bonus(litres_total)
    return payments, extra, payments + extra


def run_tests():
    assert rate_per_litre("3.50", "8.50") == Decimal("30.00")
    assert rate_per_litre("4.26", "8.74", "April-June") == Decimal("36.20")
    assert rate_per_litre("4.26", "8.74", "Original") == Decimal("33.80")
    assert payout(10, "4.26", "8.74", "April-June") == Decimal("362.00")
    assert payout(10, "4.26", "8.74", "Original") == Decimal("338.00")
    assert bonus(500) == Decimal("0.00")
    assert bonus(501) == Decimal("250.50")
    assert season_for_month(5) == "April-June" and season_for_month(9) == "Original"
    print("All Task 12 tests passed!")


if __name__ == "__main__":
    print("Worked example: 10 L, fat 4.26, SNF 8.74")
    for season in ("Original", "April-June"):
        print(f"  {season:<11} rate Rs {rate_per_litre('4.26', '8.74', season)}"
              f"   payment Rs {payout(10, '4.26', '8.74', season)}")
    print("\nBonus check: 500 L ->", bonus(500), "| 501 L ->", bonus(501))

    entries = [(60, "4.26", "8.74")] * 10          # 600 litres over ten days
    pay, extra, grand = ten_day_total(entries, "April-June")
    print(f"\nTen days (600 L, April-June): payments {pay}, bonus {extra}, grand total {grand}")
    print()
    run_tests()
