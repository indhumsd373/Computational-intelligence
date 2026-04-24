# Taking input from user
sports= int(input("Enter number of sports book: "))
maths= int(input("Enter number of maths book: "))
total=sports+maths

# Checking condition
if total == 0:
    print("Total outcomes cannot be zero")
else:
    prob_sports =sports / total
    prob_maths =maths / total
    print("P(sports) =", prob_sports)
    print("P(maths) =", prob_maths)
