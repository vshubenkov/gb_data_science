import sys
try:
    s_name, hours, bet, premium = sys.argv
except ValueError:
    print("You skipped script parameters")
    exit(0)

print("Salary: ", int(hours) * int(bet) + int(premium))