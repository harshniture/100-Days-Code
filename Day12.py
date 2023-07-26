#Take money borrowed, interest and duration as input. Then, compute the compound interest rate.

def compound_interest(principle, rate, time):
	interest = principle * ((1 + rate / 100) ** time)
	return interest

principle = int(input("P: "))
interest_rate = float(input("R: "))
time = float(input("N: "))

total_due = compound_interest(principle, interest_rate, time)

print("Interest:", total_due)