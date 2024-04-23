import random
from itertools import combinations

class Problem:
    def __init__(self, initial):
        self.initial = initial

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def goal_test(self, state):
        raise NotImplementedError

    def h(self, node):
        raise NotImplementedError

class NQueensProblem(Problem):
    def __init__(self, N):
        super().__init__(tuple([-1] * N))
        self.N = N

    def actions(self, state):
        if state[-1] != -1:
            return []
        else:
            col = state.index(-1)
            return [row for row in range(self.N) if not self.conflicted(state, row, col)]

    def result(self, state, row, col):
        new = list(state[:])
        new[col] = row
        return tuple(new)


    def conflicted(self, state, row, col):
        return any(self.conflict(row, col, state[c], c) for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        return (row1 == row2 or
                col1 == col2 or
                row1 - col1 == row2 - col2 or
                row1 + col1 == row2 + col2)

    def goal_test(self, state):
        if state[-1] == -1:
            return False
        return not any(self.conflicted(state, state[col], col) for col in range(len(state)))

    def random_state(self):
        return tuple(random.choice(range(self.N)) for _ in range(self.N))

    def fitness(self, state):
        attacking_pairs = sum(1 for i, j in combinations(range(len(state)), 2)
                          if self.conflict(state[i], i, state[j], j))
        return attacking_pairs



    def hill_climbing(self):
        current = self.initial
        while True:
            # Find the leftmost column without a queen
            col = next((i for i, x in enumerate(current) if x == -1), None)
            if col is None:  # No more columns to fill
                break

            # Generate neighbors by placing a queen in each row of this column
            neighbors = [self.result(current, row, col) for row in range(self.N)]
            if not neighbors:
                break

            neighbor = max(neighbors, key=lambda state: self.fitness(state))
            if self.fitness(neighbor) <= self.fitness(current):
                # Consider modifying this part to handle local maxima better
                break
            current = neighbor
        return current


    def random_restart_hill_climbing(self):
        count_evaluations = 0
        while True:
            self.initial = self.random_state()
            solution = self.hill_climbing()
            count_evaluations += 1
            if self.fitness(solution) == 0:
                return solution, count_evaluations

def main():
    total_evaluations = 0
    for x in range(100):
        problem = NQueensProblem(8)
        solution , evaluations = problem.random_restart_hill_climbing()
        total_evaluations += evaluations

    print("Average evaluations until a solution: ", total_evaluations / 100)

if __name__ == "__main__":
    main()
