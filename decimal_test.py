from decimal import Decimal

decimal_value = Decimal("123.45")
decimal_tuple = decimal_value.as_tuple()
print(f"{decimal_value}: {decimal_tuple}")

decimal_value = Decimal("-123.45")
decimal_tuple = decimal_value.as_tuple()
print(f"{decimal_value}: {decimal_tuple}")

decimal_value = Decimal("1234500")
decimal_tuple = decimal_value.as_tuple()
print(f"{decimal_value}: {decimal_tuple}")

decimal_value = Decimal((0, (1, 2, 3, 4, 5), 2))
decimal_tuple = decimal_value.as_tuple()
print(f"{decimal_value}: {decimal_tuple}")
