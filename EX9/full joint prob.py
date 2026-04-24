table = {
    (True, True, True): 0.168,    (True, True, False): 0.032,
    (True, False, True): 0.042,   (True, False, False): 0.018,
    (False, True, True): 0.072,   (False, True, False): 0.128,
    (False, False, True): 0.108,  (False, False, False): 0.432
}

def get_probability(query):
    # Clean the string: "P(study|exam)" -> "study|exam"
    q = query.lower().replace("p(", "").replace(")", "").replace(" ", "")
    # Split into Target (A) and Evidence (B) if '|' exists
    parts = q.split('|')
    target_vars = parts[0].split(',')
    evidence_vars = parts[1].split(',') if len(parts) > 1 else []

    def check_match(row_tuple, vars_to_check):
        s, e, p = row_tuple
        mapping = {
            'study': s, 'notstudy': not s, 'study': not s,
            'exam': e,  'notexam': not e,  'exam': not e,
            'pass': p,  'notpass': not p,  'pass': not p
        }
        return all(mapping.get(v, False) for v in vars_to_check)
    # P(A|B) = Sum(A and B) / Sum(B)
    sum_b = sum(prob for row, prob in table.items() if check_match(row, evidence_vars))
    sum_a_and_b = sum(prob for row, prob in table.items() if check_match(row, evidence_vars + target_vars))

    if sum_b == 0: return "Division by zero (Evidence probability is 0)"
    return sum_a_and_b / sum_b
# 2. User Interface
print("--- Universal Probability Query ---")
print("Example like P(study), P(pass|exam), P(study,exam|not pass),etc")
while True:
    user_input = input("\nEnter Query or 'exit': ")
    if user_input.lower() == 'exit': break

    try:
        ans = get_probability(user_input)
        print(f"Result: {ans:.4f}" if isinstance(ans, float) else ans)
    except Exception as e:
        print("Error: Please check your query format.")
