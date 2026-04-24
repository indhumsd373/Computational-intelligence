2..Bayes rule
# Taking input
p_a = float(input("Enter P(A) (prior probability): "))
p_b_given_a = float(input("Enter P(B|A): "))
p_b = float(input("Enter P(B): "))
# Check condition
if p_b == 0:
    print("P(B) cannot be zero")
else:
    p_a_given_b = (p_b_given_a * p_a) / p_b
    print("P(A|B) =", p_a_given_b)
