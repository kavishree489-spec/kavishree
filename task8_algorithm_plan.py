"""Task 8: Plan the algorithm before coding (running-total version + hand-trace check)

PSEUDOCODE - one payment
    INPUT farmer_id, litres, fat, snf
    IF litres <= 0 OR fat out of 2.0-7.0 OR snf out of 7.0-10.0 THEN
        PRINT "Invalid"
    ELSE
        fat_steps  = (fat - 3.5) / 0.1
        snf_steps  = (snf - 8.5) / 0.1
        rate       = 30 + fat_steps * 0.40 + snf_steps * 0.30
        payment    = litres * rate
        PRINT rate, payment

PSEUDOCODE - ten-day total
    total = 0
    REPEAT 10 times
        read entry; calculate payment
        total = total + payment
    PRINT total
"""
from milkrate import rate_per_litre, payout, valid_input

entries = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]

print("Hand-trace table")
print(f"{'Entry':>5} {'Litres':>7} {'Fat':>5} {'SNF':>5} {'Rate/L':>8} {'Payment':>9}")

running_total = 0.0          # approach 2: running total -> O(1) extra space
stored = []                  # approach 1: list of entries   -> O(n) space
for n, (litres, fat, snf) in enumerate(entries, 1):
    if not valid_input(litres, fat, snf):
        print(n, "Invalid")
        continue
    pay = payout(litres, fat, snf)
    running_total += pay
    stored.append(pay)
    print(f"{n:>5} {litres:>7} {fat:>5} {snf:>5} {rate_per_litre(fat, snf):>8.2f} {pay:>9.2f}")

print(f"{'Total':>5} {'':>7} {'':>5} {'':>5} {'':>8} {running_total:>9.2f}")
assert round(running_total, 2) == 917.50
assert round(sum(stored), 2) == 917.50
print("\nHand-trace total (Rs 917.50) matches the program.")
