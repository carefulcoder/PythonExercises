price = 100000
is_good_credit = True

if is_good_credit:
    down_payment = 0.1 * int(price)
    print(down_payment)
else:
    down_payment = 0.2 * int(price)
    print(f"Down Payment: ${down_payment}")