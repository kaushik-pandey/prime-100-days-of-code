principle = float(input("Enter Principal amount:\n"))
rate = float(input("Enter rate %:\n")) / 100
time = float(input("Enter Time in years:\n"))
n = float(input("Enter compound interval:\n"))
amount = principle*((1 + rate/n)**(n * time))
print(amount)
