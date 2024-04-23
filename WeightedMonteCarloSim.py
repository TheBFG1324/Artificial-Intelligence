from random import random

TRIALS = 10**6  # Number of trials for the simulation

# Probabilities as given in the Bayes Net
p_b = 0.001
p_e = 0.002

# Weights when B and E are true
weight_be = p_b * p_e

# Variables to track the weighted counts
weighted_count = 0

for trial in range(TRIALS):
    # Fix B and E to be True
    B = True
    E = True
    
    # Sample for Alarm given B and E
    randA = random()
    A = (randA < 0.98) if B and E else (randA < 0.001)
    
    # Sample for JohnCalls and MaryCalls given Alarm
    randJ = random()
    randM = random()
    J = (randJ < 0.95) if A else (randJ < 0.01)
    M = (randM < 0.7) if A else (randM < 0.01)
    
    # Check if neither John nor Mary calls
    if not J and not M:
        # Increment the weighted count
        weighted_count += 1 * weight_be

# Estimate the probability
p_no_calls_given_be = weighted_count / TRIALS
p_no_calls_and_be = p_no_calls_given_be * weight_be

print(f"Estimated P(¬J, ¬M, B, E): {p_no_calls_and_be}")
