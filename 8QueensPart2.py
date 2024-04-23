import random
from itertools import combinations

class NQueensProblem:
    def __init__(self, N):
        self.N = N
        self.initial = self.random_state()
        self.fitness_evaluations = 0

    def random_state(self):
        return tuple(random.choice(range(self.N)) for _ in range(self.N))

    def conflicted(self, state, row, col):
        return any(self.conflict(row, col, state[c], c) for c in range(self.N) if c != col)

    def conflict(self, row1, col1, row2, col2):
        return (row1 == row2 or
                col1 == col2 or
                row1 - col1 == row2 - col2 or
                row1 + col1 == row2 + col2)

    def find_conflicts(self, state):
        return [col for col in range(self.N) if self.conflicted(state, state[col], col)]

    def min_conflicts(self, state, var, value_selection='random'):
        conflicts = []
        for val in range(self.N):
            if val != state[var]:
                new_state = list(state)
                new_state[var] = val
                conflicts.append((self.fitness(tuple(new_state)), val))

        # Choose the row that leads to the highest fitness (fewest conflicts)
        max_fitness = max(conflicts)[0]
        best_rows = [val for fit, val in conflicts if fit == max_fitness]

        # If multiple best rows, choose randomly
        return random.choice(best_rows)

    def fitness(self, state):
        self.fitness_evaluations+=1
        attacking_pairs = sum(1 for i, j in combinations(range(len(state)), 2)
                              if self.conflict(state[i], i, state[j], j))
        return 28 - attacking_pairs

    def solve(self, selection='random'):
        state = self.initial
        current_col = 0  # Start with the first column for cyclic selection

        for iterations in range(1000):  # Set a maximum number of iterations
            conflicts = self.find_conflicts(state)
            if not conflicts:
                return state, self.fitness_evaluations  # Solution found

            if selection == 'random':
                var = random.choice(conflicts)
            else:  # Cyclic selection
                while current_col not in conflicts:
                    current_col = (current_col + 1) % self.N
                var = current_col
                current_col = (current_col + 1) % self.N

            val = self.min_conflicts(state, var, value_selection=selection)
            state = list(state)
            state[var] = val
            state = tuple(state)

        return None, None  # Solution not found


def main():
    for selection in ['random', 'cyclic']:
        total_evaluations = 0
        number_of_fails = 0
        for _ in range(100):
            problem = NQueensProblem(8)
            solution, evals = problem.solve(selection)
            if solution:
                total_evaluations += evals
            else:
                number_of_fails+=1
        print(f"Average evaluations for {selection} selection: {total_evaluations / 100}")
        print("percent of Fails: ", number_of_fails/100)
if __name__ == "__main__":
    main()
