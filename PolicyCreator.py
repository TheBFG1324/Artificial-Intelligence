# MS Branicky, 2020-04-06

# please double-check before using

# States in 4x3 grid world are defined as follows:
#    3  5  8  11
#    2     7  10
#    1  4  6   9


Up, Left, Right, Down = 1, 2, 3, 4
# Tdict[s,a,snext] = probability of that transition
Tdict = dict()
for a in range(1,5):
    Tdict[10,a,10] = 1
    Tdict[11,a,11] = 1

Tdict[1,Up,2] = 0.8
Tdict[1,Up,1] = 0.1
Tdict[1,Up,4] = 0.1
Tdict[2,Up,3] = 0.8
Tdict[2,Up,2] = 0.2
Tdict[3,Up,3] = 0.9
Tdict[3,Up,5] = 0.1
Tdict[4,Up,4] = 0.8
Tdict[4,Up,1] = 0.1
Tdict[4,Up,6] = 0.1
Tdict[5,Up,5] = 0.8
Tdict[5,Up,3] = 0.1
Tdict[5,Up,8] = 0.1
Tdict[6,Up,7] = 0.8
Tdict[6,Up,4] = 0.1
Tdict[6,Up,9] = 0.1
Tdict[7,Up,8] = 0.8
Tdict[7,Up,7] = 0.1
Tdict[7,Up,10] = 0.1
Tdict[8,Up,8] = 0.8
Tdict[8,Up,5] = 0.1
Tdict[8,Up,11] = 0.1
Tdict[9,Up,10] = 0.8
Tdict[9,Up,6] = 0.1
Tdict[9,Up,9] = 0.1
Tdict[1,Left,1] = 0.9
Tdict[1,Left,2] = 0.1
Tdict[2,Left,2] = 0.8
Tdict[2,Left,3] = 0.1
Tdict[2,Left,1] = 0.1
Tdict[3,Left,3] = 0.9
Tdict[3,Left,2] = 0.1
Tdict[4,Left,1] = 0.8
Tdict[4,Left,4] = 0.2
Tdict[5,Left,3] = 0.8
Tdict[5,Left,5] = 0.2
Tdict[6,Left,4] = 0.8
Tdict[6,Left,7] = 0.1
Tdict[6,Left,6] = 0.1
Tdict[7,Left,7] = 0.8
Tdict[7,Left,8] = 0.1
Tdict[7,Left,6] = 0.1
Tdict[8,Left,5] = 0.8
Tdict[8,Left,7] = 0.1
Tdict[8,Left,8] = 0.1
Tdict[9,Left,6] = 0.8
Tdict[9,Left,10] = 0.1
Tdict[9,Left,9] = 0.1
Tdict[1,Right,4] = 0.8
Tdict[1,Right,1] = 0.1
Tdict[1,Right,2] = 0.1
Tdict[2,Right,2] = 0.8
Tdict[2,Right,1] = 0.1
Tdict[2,Right,3] = 0.1
Tdict[3,Right,5] = 0.8
Tdict[3,Right,3] = 0.1
Tdict[3,Right,2] = 0.1
Tdict[4,Right,6] = 0.8
Tdict[4,Right,4] = 0.2
Tdict[5,Right,8] = 0.8
Tdict[5,Right,5] = 0.2
Tdict[6,Right,9] = 0.8
Tdict[6,Right,7] = 0.1
Tdict[6,Right,6] = 0.1
Tdict[7,Right,10] = 0.8
Tdict[7,Right,8] = 0.1
Tdict[7,Right,6] = 0.1
Tdict[8,Right,11] = 0.8
Tdict[8,Right,7] = 0.1
Tdict[8,Right,8] = 0.1
Tdict[9,Right,9] = 0.9
Tdict[9,Right,10] = 0.1
Tdict[1,Down,1] = 0.9
Tdict[1,Down,4] = 0.1
Tdict[2,Down,1] = 0.8
Tdict[2,Down,2] = 0.2
Tdict[3,Down,2] = 0.8
Tdict[3,Down,5] = 0.1
Tdict[3,Down,8] = 0.1
Tdict[4,Down,4] = 0.8
Tdict[4,Down,1] = 0.1
Tdict[4,Down,6] = 0.1
Tdict[5,Down,5] = 0.8
Tdict[5,Down,3] = 0.1
Tdict[5,Down,8] = 0.1
Tdict[6,Down,6] = 0.8
Tdict[6,Down,4] = 0.1
Tdict[6,Down,9] = 0.1
Tdict[7,Down,6] = 0.8
Tdict[7,Down,7] = 0.1
Tdict[7,Down,10] = 0.1
Tdict[8,Down,7] = 0.8
Tdict[8,Down,5] = 0.1
Tdict[8,Down,11] = 0.1
Tdict[9,Down,9] = 0.9
Tdict[9,Down,6] = 0.1

def T(s,a,snext):
    if (s,a,snext) in Tdict:
        return Tdict[s,a,snext]
    return 0

for s in range(1, 12):
    for a in range(1, 5):
        cumulative = 0
        for nexts in range(1, 12):
            tmp = T(s, a, nexts)
            cumulative += tmp  # This line should be indented to be inside the for-loop
            if tmp > 0:
                print("T( %2d, %2d, %2d ) = %.1f" % (s, a, nexts, T(s, a, nexts)))
    assert cumulative == 1, (s, a, nexts, cumulative)  # This should be inside the for-loop for actions


# Let's define the rewards and terminal states
R = -1
states_rewards = {10: -1, 11: 1}
gamma = 1.0
threshold = 0.000001 # convergence threshold

def T(s, a, snext):
    prob = Tdict.get((s, a, snext), 0)
    return prob


# Value Iteration Algorithm for a 4x3 grid world as described

# Initialize utilities for all states
U = {s: R for s in range(1, 12)}
U[10], U[11] = -1, +1  # Terminal states

# Initialize policy
policy = {s: None for s in range(1, 12)}
policy[10], policy[11] = 'Terminal', 'Terminal'  # Terminal states


def expected_utility(s, a, U):
    return sum(T(s, a, nexts) * U[nexts] for nexts in range(1, 12) if T(s, a, nexts) > 0)

# Begin the value iteration loop
while True:
    U_prime = U.copy()
    delta = 0
    for s in range(1, 12):
        if s in states_rewards:  # Skip the terminal states
            continue

        action_utilities = [(a, expected_utility(s, a, U)) for a in range(1, 5)]

        # Select the action with the highest expected utility
        best_action, best_utility = max(action_utilities, key=lambda x: x[1])
        
        U_prime[s] = R + gamma * best_utility
        policy[s] = best_action
        delta = max(delta, abs(U_prime[s] - U[s]))

    if delta < threshold:
        break

    U = U_prime

for s in range(1, 12):
    print(f"Utility of state {s}: {U[s]}")
    print(f"Policy for state {s}: {policy[s]}")
