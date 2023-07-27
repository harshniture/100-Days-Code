#You borrowed $5000 for 2 years with 2% interest per year. Calculate the simple interest to know how much you have to pay?

principle = int(input("P: "))
interest_rate = float(input("R: "))
time = float(input("N: "))

# Calculates simple interest
simple_interest = principle * (interest_rate/100) * time

print("Simple Interest:", simple_interest)