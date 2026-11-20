"""Task 9: automated tests using assert. Run:  python test_milkrate.py"""
from milkrate import rate_per_litre, payout, valid_input, ten_day_total


def test_calculator():
    assert rate_per_litre(4.2, 8.7) == 33.40
    assert rate_per_litre(3.1, 8.3) == 27.80
    assert payout(10, 3.5, 8.5) == 300.00
    assert payout(10, 4.2, 8.7) == 334.00
    assert payout(12, 3.1, 8.3) == 333.60
    assert payout(10.5, 4.2, 8.7) == 350.70
    assert rate_per_litre(2.0, 8.5) == 24.00
    assert rate_per_litre(7.0, 8.5) == 44.00
    assert valid_input(-5, 3.5, 8.5) is False
    assert valid_input(10, 1.9, 8.5) is False
    assert valid_input(10, 7.1, 8.5) is False
    assert valid_input("abc", 3.5, 8.5) is False
    assert valid_input(10, 3.5, 8.5) is True
    payments = [300.00, 283.90, 333.60, 150.00, 193.80]
    assert ten_day_total(payments) == 1261.30
    print("All tests passed!")


test_calculator()
