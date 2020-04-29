has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for Loan")

# and is both
# or is at least one
# not (if good credit and no criminal record)

if has_good_credit and not has_criminal_record:
    print("Eligible for Loan")
else:
    print("Not eligible for Loan")