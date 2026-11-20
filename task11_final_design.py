"""Task 11: Recommended final design - Decimal, rounding policy, rate card in a JSON file"""
import json
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")


def load_rate_card(path="rate_card.json"):
    """Load and validate the rate card (rates can change without editing code)."""
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    required = ["base_rate", "base_fat", "base_snf", "fat_adjustment", "snf_adjustment"]
    missing = [key for key in required if key not in raw]
    if missing:
        raise ValueError(f"Rate card is missing: {missing}")
    return {key: Decimal(str(raw[key])) for key in required}


def rate_per_litre(card, fat, snf):
    fat_steps = (Decimal(fat) - card["base_fat"]) / Decimal("0.1")
    snf_steps = (Decimal(snf) - card["base_snf"]) / Decimal("0.1")
    return (card["base_rate"] + fat_steps * card["fat_adjustment"]
            + snf_steps * card["snf_adjustment"])


def payment(card, litres, fat, snf):
    """Round each payable amount to 2 places (ROUND_HALF_UP)."""
    amount = Decimal(litres) * rate_per_litre(card, fat, snf)
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


if __name__ == "__main__":
    # Rounding example
    amount = Decimal("33.405")
    print("33.405 rounded half-up ->", amount.quantize(CENT, rounding=ROUND_HALF_UP))

    card = load_rate_card()
    print("Rate card loaded:", {k: str(v) for k, v in card.items()})

    entries = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7"), ("12", "3.1", "8.3")]
    total = Decimal("0")
    for litres, fat, snf in entries:
        pay = payment(card, litres, fat, snf)
        total += pay                       # add the already-rounded payments
        print(f"{litres:>5} L  fat {fat}  snf {snf}  rate {rate_per_litre(card, fat, snf):.2f}  pay {pay}")
    print("Total:", total)
    assert total == Decimal("917.50")

    # Scale check: 150,000 entries is O(n)
    import time
    start = time.perf_counter()
    big_total = Decimal("0")
    for _ in range(150000):
        big_total += payment(card, "10", "4.2", "8.7")
    print(f"150,000 payments total Rs {big_total} in {time.perf_counter() - start:.2f} s")
