"""Task 10: Compare expectations with execution (float vs Decimal)"""
import time
from decimal import Decimal, ROUND_HALF_UP

PAYMENT_FLOAT = 33.40
PAYMENT_DECIMAL = Decimal("33.40")

print(f"{'Payments':>9} {'Expected':>15} {'Float total':>17} {'Decimal total':>15} "
      f"{'Float s':>9} {'Decimal s':>10}")

for n in (300, 6000, 150000):
    expected = PAYMENT_DECIMAL * n

    start = time.perf_counter()
    float_total = 0.0
    for _ in range(n):
        float_total += PAYMENT_FLOAT
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    decimal_total = Decimal("0")
    for _ in range(n):
        decimal_total += PAYMENT_DECIMAL
    decimal_time = time.perf_counter() - start

    print(f"{n:>9} {expected:>15,.2f} {float_total:>17,.2f} {decimal_total:>15,.2f} "
          f"{float_time:>9.5f} {decimal_time:>10.5f}")
    print(f"          float error vs expected: {float_total - float(expected):.12f}")

# Rounding each payment vs rounding only the final total
print("\nRounding each payment vs rounding the final total")
raw = [Decimal("33.405")] * 3
cent = Decimal("0.01")
each_rounded = sum(p.quantize(cent, rounding=ROUND_HALF_UP) for p in raw)
total_rounded = sum(raw).quantize(cent, rounding=ROUND_HALF_UP)
print("Round each payment, then add :", each_rounded)
print("Add, then round the total    :", total_rounded)

# Alternative design: rate dictionary (calculate each (fat, snf) rate only once)
print("\nRate dictionary (cache)")
rate_cache = {}


def cached_rate(fat, snf):
    key = (fat, snf)
    if key not in rate_cache:
        fat_steps = (Decimal(fat) - Decimal("3.5")) / Decimal("0.1")
        snf_steps = (Decimal(snf) - Decimal("8.5")) / Decimal("0.1")
        rate_cache[key] = (Decimal("30.00") + fat_steps * Decimal("0.40")
                           + snf_steps * Decimal("0.30"))
    return rate_cache[key]


start = time.perf_counter()
total = Decimal("0")
for _ in range(150000):
    total += Decimal("10") * cached_rate("4.2", "8.7")
print("150000 entries with cache, total =", total,
      f"time = {time.perf_counter() - start:.5f} s, rates calculated = {len(rate_cache)}")
