from random import random

TRIALS = 10**6  

qualified_observed = 0  
admitted_observed = 0  

for trial in range(TRIALS):
    
    randA, randB, randC, randD = (random() for i in range(4))
    
    
    A = (randA < 0.5)
    
    
    B = A or (randB < 0.5)
    
    
    C = A or (randC < 0.5)
    
    
    D = None
    if B and C:
        D = True
    elif not B and not C:
        D = (randD < 0.0)
    elif B and not C:
        D = (randD < 0.5)
    elif not B and C:
        D = (randD < 0.5)
    
    
    if D:
        admitted_observed += 1
        if A:
            qualified_observed += 1


p_a_given_d = qualified_observed / admitted_observed if admitted_observed > 0 else 0

print(f"P(A|D) ~ {p_a_given_d}")
